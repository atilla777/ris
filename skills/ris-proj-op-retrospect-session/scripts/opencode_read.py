"""Protected-state read-only OpenCode boundary; scoped CLI service effects only."""

import json
import hashlib
import os
import re
import time
import subprocess
import urllib.request
import urllib.parse
import urllib.error
import argparse
import sys
from collections import deque
from typing import TypeGuard

MAX_BYTES = 64 * 1024 * 1024
MAX_JSON_DEPTH = 128
V2_BASELINE = "2.0.32"


def v2_version(value):
    return isinstance(value, str) and re.fullmatch(r"2\.\d+\.\d+", value) is not None


class Captured(bytes):
    """Keep the producing CLI version out of the original transcript bytes."""

    source_version: str


def identifier(value, prefix):
    if not isinstance(value, str) or not re.fullmatch(prefix + r"_[A-Za-z0-9]+", value):
        raise ReadError("invalid identifier")
    return value


class ReadError(ValueError):
    """A secret-safe source diagnostic."""


class SourceConflict(ReadError):
    """Contradictory source identity or explicit version binding."""


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ReadError("duplicate JSON key")
        result[key] = value
    return result


def decode_json(raw, diagnostic):
    """Reject ambiguous objects at the first boundary, before normalization."""
    try:
        if len(raw) > MAX_BYTES:
            raise ReadError("source byte limit exceeded; no content processed")
        text = raw.decode("utf-8-sig") if isinstance(raw, bytes) else raw
        if len(text.encode("utf-8")) > MAX_BYTES:
            raise ReadError("source byte limit exceeded; no content processed")
        # This lexical pass runs before the recursive stdlib decoder. Brackets
        # inside strings and escaped quotes do not contribute to nesting.
        depth = 0
        quoted = escaped = False
        for char in text:
            if quoted:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    quoted = False
            elif char == '"':
                quoted = True
            elif char in "[{":
                depth += 1
                if depth > MAX_JSON_DEPTH:
                    raise ReadError("JSON nesting limit exceeded")
            elif char in "]}":
                depth = max(0, depth - 1)
        return json.loads(text, object_pairs_hook=unique_object)
    except ReadError:
        raise
    except RecursionError:
        raise ReadError("JSON nesting limit exceeded") from None
    except (ValueError, UnicodeError, TypeError):
        raise ReadError(diagnostic) from None


def check_structure(value):
    """Depth-first iterators bound stack space and reject cycles by depth."""
    stack = [(iter([value]), 0)]
    while stack:
        nodes, depth = stack[-1]
        try:
            node = next(nodes)
        except StopIteration:
            stack.pop()
            continue
        if isinstance(node, (dict, list, tuple)):
            if depth >= MAX_JSON_DEPTH:
                raise ReadError("JSON nesting limit exceeded")
            stack.append(
                (iter(node.values() if isinstance(node, dict) else node), depth + 1)
            )


def encode_json(value, **kwargs):
    check_structure(value)
    try:
        return json.dumps(value, **kwargs)
    except RecursionError:
        raise ReadError("JSON nesting limit exceeded") from None
    except (ValueError, TypeError, UnicodeError):
        raise ReadError("invalid JSON value") from None


def pages(source, cursor=None, budget=8192):
    if (
        not isinstance(budget, int)
        or isinstance(budget, bool)
        or not 1 <= budget <= 65536
    ):
        raise ReadError("invalid page budget")
    event, offset = 0, 0
    if cursor is not None:
        if (
            not isinstance(cursor, dict)
            or cursor.get("fingerprint") != source["fingerprint"]
            or cursor.get("view", "all") != source.get("view", "all")
        ):
            raise ReadError("snapshot conflict")
        event, offset = cursor.get("event"), cursor.get("offset")
        if type(event) is not int or type(offset) is not int or event < 0 or offset < 0:
            raise ReadError("invalid cursor")
    events = source["events"]
    items = []
    remaining = budget
    if event > len(events) or (
        event < len(events) and offset >= len(events[event]["content"])
    ):
        raise ReadError("invalid cursor range")
    while event < len(events) and remaining:
        e = events[event]
        end = min(len(e["content"]), offset + remaining)
        items.append(
            {
                "ref": e["ref"],
                "type": e["type"],
                "range": [offset, end],
                "total": len(e["content"]),
                "content": e["content"][offset:end],
                "temporal": e["temporal"],
            }
        )
        remaining -= end - offset
        if end == len(e["content"]):
            event += 1
            offset = 0
        else:
            offset = end
    continuation = (
        None
        if event == len(events)
        else {
            "fingerprint": source["fingerprint"],
            "view": source.get("view", "all"),
            "event": event,
            "offset": offset,
        }
    )
    return {
        "fingerprint": source["fingerprint"],
        "items": items,
        "next": continuation,
        "coverage": "returned content only; agent observation not established",
    }


def safe(value):
    """Defense in depth, not a universal secret detector; refs remain preferred."""
    check_structure(value)
    try:
        return _redact(value)
    except RecursionError:
        raise ReadError("JSON nesting limit exceeded") from None
    except (ValueError, TypeError, UnicodeError):
        raise ReadError("invalid JSON value") from None


def _redact(value):
    if isinstance(value, dict):
        return {
            k: (
                "[REDACTED]"
                if re.search(
                    r"(?i)secret|password|authorization|api.?key|access.?token", k
                )
                else _redact(v)
            )
            for k, v in value.items()
        }
    if isinstance(value, list):
        return [_redact(v) for v in value]
    if isinstance(value, str):
        value = re.sub(
            r"(?i)((?:secret|password|token|api[_-]?key|authorization)\s*[:=]\s*)\S+",
            r"\1[REDACTED]",
            value,
        )
        return re.sub(
            r"\b(?:sk-[A-Za-z0-9_-]{8,}|CANARY[A-Za-z0-9_-]*)\b", "[REDACTED]", value
        )
    return value


def temporal(obj, cutoff=None, boundary=False):
    if cutoff is None:
        return "snapshot"
    if boundary:
        return "captured-boundary"
    interval = obj.get("time", {})
    if not isinstance(interval, dict):
        interval = {}
    start = interval.get("start", interval.get("created"))
    end = interval.get("end", interval.get("completed"))
    if number(start) and start > cutoff:
        return "after-cutoff"
    if number(start) and number(end) and start <= end <= cutoff:
        return "before-cutoff"
    if number(start) and start <= cutoff and (not number(end) or end > cutoff):
        return "pending-at-cutoff; late evidence"
    return "unknown-at-cutoff; late evidence"


def number(value) -> TypeGuard[int | float]:
    return type(value) in (int, float) and value >= 0 and value < float("inf")


def check_boundary_time(obj, cutoff, boundary):
    interval = obj.get("time", {})
    if not isinstance(interval, dict):
        raise ReadError("unsupported event time")
    if (
        boundary
        and cutoff is not None
        and any(
            number(interval.get(key)) and interval[key] > cutoff
            for key in (
                "created",
                "updated",
                "completed",
                "start",
                "end",
                "compacted",
                "streamed",
                "ran",
                "idle",
                "viewed",
                "archived",
            )
        )
    ):
        raise ReadError("boundary snapshot conflict")


def usage_reading(tokens, provenance, supported):
    tokens = tokens if isinstance(tokens, dict) else {}
    cache = tokens.get("cache", {})
    cache = cache if isinstance(cache, dict) else {}
    raw = {
        "input": tokens.get("input"),
        "cache_read": cache.get("read"),
        "cache_write": cache.get("write"),
        "output": tokens.get("output"),
        "reasoning": tokens.get("reasoning"),
    }
    fields = {key: value if number(value) else None for key, value in raw.items()}
    known = [
        value
        for key in ("input", "cache_read", "cache_write")
        if number(value := fields[key])
    ]
    context = sum(known) if supported and known and sum(known) > 0 else None
    quality = (
        "known"
        if context is not None and len(known) == 3
        else "lower-bound"
        if context is not None
        else "unknown"
    )
    return {
        "provenance": provenance,
        "fields": fields,
        "context": context,
        "quality": quality,
    }


def metrics(source, cutoff=None, boundary=False):
    requests = []
    spans = []
    tools = []
    task_wait = []
    gaps = []
    threshold_evidence = []
    is_v2 = source.get("format") == "v2"
    supported = source["version"] == "1.18.33" or (
        is_v2 and source["version"] == V2_BASELINE
    )
    sums: dict[str, int | float] = {
        k: 0 for k in ("input", "cache_read", "cache_write", "output", "reasoning")
    }
    counts = dict.fromkeys(sums, 0)
    for m in source["data"]["messages"]:
        mi = m["info"]
        mid = mi["id"]
        mt = mi.get("time", {})
        if (
            mi.get("role") == "assistant"
            and valid_interval(mt.get("created"), mt.get("completed"))
            and (cutoff is None or boundary or temporal(mi, cutoff) == "before-cutoff")
        ):
            spans.append((mt["created"], mt["completed"]))
        steps = (
            ([mi] if mi.get("role") in ("assistant", "compaction") else [])
            if is_v2
            else [p for p in m["parts"] if p.get("type") == "step-finish"]
        )
        if is_v2 and mi.get("retry"):
            gaps.append(
                {
                    "ref": f"{source['session']}/{mid}",
                    "kind": "unmeasured-retry-attempts",
                }
            )
        for p in m["parts"]:
            if p.get("type") == "tool":
                interval = p.get("state", {}).get("time", {})
                if valid_interval(interval.get("start"), interval.get("end")) and (
                    cutoff is None
                    or boundary
                    or temporal({"time": interval}, cutoff) == "before-cutoff"
                ):
                    (task_wait if p.get("tool") == "task" else tools).append(
                        (interval["start"], interval["end"])
                    )
        for p in steps:
            ref = f"{source['session']}/{mid}" + ("" if is_v2 else f"/{p['id']}")
            timing = temporal(p, cutoff, boundary)
            # A completed assistant message establishes an upper bound for its steps.
            if cutoff is not None and temporal(mi, cutoff) == "before-cutoff":
                timing = "before-cutoff"
            tokens = p.get("tokens")
            provenance = ref
            message_tokens = mi.get("tokens", {})
            message_ref = f"{source['session']}/{mid}"
            step_reading = usage_reading(tokens, ref, supported)
            message_reading = usage_reading(message_tokens, message_ref, supported)
            if is_v2:
                for reading in (step_reading, message_reading):
                    if reading["context"] is not None:
                        reading["quality"] = "lower-bound"
            readings = [step_reading] + (
                [message_reading] if len(steps) == 1 and not is_v2 else []
            )
            conflicting_fields = []
            step_measured = any(
                number(value) and value > 0 for value in step_reading["fields"].values()
            )
            message_measured = any(
                number(value) and value > 0
                for value in message_reading["fields"].values()
            )
            if supported and len(steps) == 1 and step_measured and message_measured:
                conflicting_fields = [
                    key
                    for key, value in step_reading["fields"].items()
                    if value is not None
                    and message_reading["fields"][key] is not None
                    and value != message_reading["fields"][key]
                ]
            selected = step_reading
            if (
                len(steps) == 1
                and not conflicting_fields
                and message_reading["context"] is not None
                and (
                    step_reading["context"] is None
                    or (
                        step_reading["quality"] == "lower-bound"
                        and (
                            message_reading["quality"] == "known"
                            or message_reading["context"] > step_reading["context"]
                        )
                    )
                )
            ):
                selected = message_reading
                provenance = message_ref + " single-step fallback"
            fields = selected["fields"]
            eligible = supported and (
                cutoff is None or timing in ("before-cutoff", "captured-boundary")
            )
            context = (
                selected["context"] if eligible and not conflicting_fields else None
            )
            quality = (
                "conflict"
                if conflicting_fields
                else selected["quality"]
                if context is not None
                else "unknown"
            )
            if is_v2 and context is not None:
                # V2 normalizes absent provider components to zero. Preserve the
                # measured positive bound, not a claim of complete provider usage.
                quality = "lower-bound"
            requests.append(
                {
                    "ref": ref,
                    "provenance": provenance,
                    "context": context,
                    "quality": quality,
                    "temporal": timing,
                    "readings": readings,
                    "conflicting_fields": conflicting_fields,
                }
            )
            if conflicting_fields:
                gaps.append(
                    {
                        "ref": ref,
                        "kind": "usage-conflict",
                        "message_ref": message_ref,
                        "fields": conflicting_fields,
                        "temporal": timing,
                    }
                )
            if eligible:
                candidates = readings if conflicting_fields else [selected]
                for reading in candidates:
                    if reading["context"] is not None and reading["context"] > 150000:
                        threshold_evidence.append(
                            {
                                key: reading[key]
                                for key in ("provenance", "context", "quality")
                            }
                            | {
                                "basis": "conflicting-reading"
                                if conflicting_fields
                                else "request-reading"
                            }
                        )
            if eligible and context is not None:
                for k, v in fields.items():
                    if number(v):
                        sums[k] += v
                        counts[k] += 1
            if context is None and not conflicting_fields:
                gaps.append({"ref": ref, "kind": "unknown-request-usage"})
        if not steps and mi.get("role") == "assistant":
            gaps.append(
                {
                    "ref": f"{source['session']}/{mid}",
                    "kind": "request-enumeration-unknown",
                }
            )
    known_requests = [p for p in requests if p["context"] is not None]
    conflicting_requests = sum(bool(p["conflicting_fields"]) for p in requests)
    peak = max((p["context"] for p in known_requests), default=None)
    complete = (
        bool(requests)
        and len(known_requests) == len(requests)
        and all(p["quality"] == "known" for p in requests)
        and not gaps
    )
    return {
        "session": source["session"],
        "semantics": (
            "2.0.32 assistant/compaction-step normalized noncached input + cache.read + cache.write; missing provider components may be zero; unrecorded attempts excluded"
            if is_v2
            else "1.18.33 noncached input + cache.read + cache.write"
        )
        if supported
        else "unknown version",
        "peak": peak,
        "peak_quality": "conflict"
        if conflicting_requests
        else "known"
        if complete
        else "lower-bound"
        if peak is not None
        else "unknown",
        "peak_scope": "unconflicted known requests only",
        "peak_lower_bound": peak,
        "threshold_signal": bool(threshold_evidence),
        "threshold_evidence": threshold_evidence,
        "threshold_meaning": "investigate eligible readings; conflicting evidence does not prove actual exceedance",
        "conflicting_requests": conflicting_requests,
        "requests": requests,
        "known_requests": len(known_requests),
        "enumerated_requests": len(requests),
        "context_sum": sum(p["context"] for p in known_requests)
        if known_requests
        else None,
        "sums": {
            k: {"value": sums[k] if counts[k] else None, "known_requests": counts[k]}
            for k in sums
        },
        "sum_quality": "known" if complete else "known subset/lower bound",
        "gaps": gaps,
        "time": {
            "unit": "milliseconds",
            "assistant_elapsed_union": union(spans),
            "tool_union": union(tools),
            "parent_task_wait_union": union(task_wait),
            "assistant_intervals": spans,
            "tool_intervals": tools,
            "task_wait_intervals": task_wait,
            "human_external_wait": None,
            "limitations": "elapsed is not generation/thinking; waits need content evidence; categories overlap; unclassified gaps remain; V2 parent task wait is delegation-call lifetime only, not background child runtime",
        },
    }


def union(intervals):
    total = 0
    start = end = None
    for a, b in sorted(intervals):
        if not valid_interval(a, b):
            raise ReadError("invalid interval")
        if end is None:
            start, end = a, b
        elif a <= end:
            end = max(end, b)
        else:
            total += end - start
            start, end = a, b
    return total + (end - start if end is not None else 0)


def valid_interval(start, end):
    return number(start) and number(end) and start <= end


def cli_capture(
    project,
    operation,
    session=None,
    executable="opencode",
    use_memfd=True,
    timeout=30,
    endpoint=None,
    query=None,
):
    # Caller authorizes fixed standard-client reads and accepts ordinary service
    # effects. No initialization witness, SQL/bootstrap or blanket write grant.
    if operation == "api":
        validate_v2_get(session, query)
        # V2 raw method/path mode ignores --param (it only interpolates operation
        # IDs). Put the validated query in the path, or pagination/filtering lies.
        path = session + ("?" + urllib.parse.urlencode(query) if query else "")
        args = ["api", "get", path]
    elif operation == "export":
        args = ["export", identifier(session, "ses")]
    elif operation == "list":
        args = ["session", "list", "--format", "json", "--max-count", "5"]
    else:
        raise ReadError("CLI operation not allowed")
    kwargs = {
        "cwd": project,
        "shell": False,
        "stderr": subprocess.PIPE,
        "timeout": timeout,
    }
    try:
        version = subprocess.run(
            [executable, "--version"], stdout=subprocess.PIPE, **kwargs
        )
        version_text = version.stdout.decode("ascii", errors="replace").strip()
        version_text = re.sub(r"^opencode v?", "", version_text)
        is_v2 = v2_version(version_text)
        if version.returncode != 0 or not (version_text == "1.18.33" or is_v2):
            raise ReadError("unsupported CLI version")
        if is_v2 and operation == "export":
            args = ["session", "export", identifier(session, "ses")]
        if endpoint:
            validate_endpoint(endpoint)
            if not is_v2:
                raise ReadError("explicit CLI server requires V2")
            args.extend(["--server", endpoint])
        if operation == "api" and not is_v2:
            raise ReadError("API client requires V2")
        command = [executable] + ([] if is_v2 else ["--pure"]) + args
        if use_memfd and hasattr(os, "memfd_create"):
            with os.fdopen(
                os.memfd_create("ris-opencode-read", os.MFD_CLOEXEC), "w+b"
            ) as output:
                result = subprocess.run(command, stdout=output, **kwargs)
                output.seek(0)
                raw = output.read(MAX_BYTES + 1)
        else:
            result = subprocess.run(command, stdout=subprocess.PIPE, **kwargs)
            raw = result.stdout
        if result.returncode != 0:
            raise ReadError("CLI read failed")
        if len(raw) > MAX_BYTES:
            raise ReadError("source byte limit exceeded; no content processed")
        captured = Captured(raw)
        captured.source_version = version_text
        return captured
    except (OSError, subprocess.TimeoutExpired):
        raise ReadError("CLI unavailable or timed out") from None


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def validate_endpoint(endpoint):
    base = urllib.parse.urlsplit(endpoint)
    if (
        base.scheme not in ("http", "https")
        or not base.hostname
        or base.username
        or base.password
        or base.query
        or base.fragment
        or base.path not in ("", "/")
    ):
        raise ReadError("invalid endpoint scope")


def get_json(endpoint, project, path, timeout=30, query=None):
    validate_endpoint(endpoint)
    is_v2 = path.startswith("/api/")
    if is_v2:
        validate_v2_get(path, query)
    elif not re.fullmatch(
        r"/session/status|/session/ses_[A-Za-z0-9]+(?:/children|/message(?:/msg_[A-Za-z0-9]+)?)?",
        path,
    ):
        raise ReadError("GET path not allowed")
    url = (
        endpoint.rstrip("/")
        + path
        + "?"
        + urllib.parse.urlencode(
            query or {} if is_v2 else {"directory": os.path.realpath(project)}
        )
    )
    request = urllib.request.Request(
        url, method="GET", headers={"Accept": "application/json"}
    )
    opener = urllib.request.build_opener(NoRedirect(), urllib.request.ProxyHandler({}))
    try:
        with opener.open(request, timeout=timeout) as response:
            if response.headers.get("Link") or response.headers.get("X-Next-Cursor"):
                raise ReadError("partial GET response; pagination not verified")
            raw = response.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                raise ReadError("source byte limit exceeded; no content processed")
            return decode_json(raw, "GET failed or invalid JSON")
    except ReadError:
        raise
    except urllib.error.HTTPError as error:
        error.close()
        raise ReadError("GET failed or invalid JSON") from None
    except (OSError, ValueError):
        raise ReadError("GET failed or invalid JSON") from None


def list_rows(raw, project, limit=5):
    if not raw.strip():
        return []
    rows = decode_json(raw, "invalid list JSON")
    if not isinstance(rows, list):
        raise ReadError("unsupported list schema")
    found = []
    seen = set()
    for row in rows:
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("directory"), str)
            or not number(row.get("updated"))
        ):
            raise ReadError("unsupported list row")
        sid = identifier(row.get("id"), "ses")
        if sid in seen:
            raise ReadError("duplicate list session")
        seen.add(sid)
        if os.path.realpath(row["directory"]) == os.path.realpath(project):
            found.append(safe(row))
    return sorted(found, key=lambda row: (-row["updated"], row["id"]))[:limit]


def participants(root, sources, cutoff=None, boundary=False, children=None):
    found = []
    gaps = []
    links = []
    linked_pairs = set()
    visited = set()
    queue = deque([root])
    while queue:
        source = queue.popleft()
        sid = source["session"]
        if sid in visited:
            continue
        visited.add(sid)
        found.append(sid)
        candidates = []
        for m in source["data"]["messages"]:
            for p in m["parts"]:
                if p.get("type") != "tool" or p.get("tool") != "task":
                    continue
                meta = p.get("state", {}).get("metadata", {})
                child = meta.get("sessionId")
                declared = meta.get("parentSessionId")
                if not child:
                    gaps.append({"kind": "missing-task-link", "session": sid})
                    continue
                try:
                    identifier(child, "ses")
                except ReadError:
                    gaps.append({"kind": "invalid-task-link", "session": sid})
                    continue
                candidates.append(
                    (
                        child,
                        declared,
                        temporal(
                            p.get("state", {}),
                            cutoff,
                            boundary and source.get("boundary", boundary),
                        ),
                        p["id"],
                    )
                )
        if children is None or sid not in children:
            gaps.append({"kind": "children-enumeration-unavailable", "session": sid})
        else:
            candidates.extend(
                (
                    c,
                    sid,
                    "snapshot"
                    if cutoff is None
                    else "unknown-at-cutoff; late evidence",
                    "GET children",
                )
                for c in children[sid]
            )
        for child, declared, timing, ref in candidates:
            other = sources.get(child)
            if other is None:
                gaps.append({"kind": "missing-child", "session": child, "parent": sid})
                continue
            if declared != sid or other["data"]["info"].get("parentID") != sid:
                gaps.append({"kind": "foreign-parent", "session": child, "parent": sid})
                continue
            parent_project = source["data"]["info"].get("projectID")
            if (
                parent_project is not None
                and other["data"]["info"].get("projectID") != parent_project
            ):
                gaps.append(
                    {"kind": "foreign-project", "session": child, "parent": sid}
                )
                continue
            if other["data"]["info"].get("fork"):
                gaps.append(
                    {"kind": "fork-not-participant", "session": child, "parent": sid}
                )
                continue
            if (sid, child) in linked_pairs:
                continue
            linked_pairs.add((sid, child))
            links.append(
                {"parent": sid, "child": child, "ref": ref, "temporal": timing}
            )
            if child in visited:
                gaps.append({"kind": "reused-or-cycle", "session": child})
                continue
            if cutoff is not None and timing not in (
                "before-cutoff",
                "captured-boundary",
            ):
                gaps.append({"kind": "late-child-link", "session": child})
                continue
            queue.append(other)
    return {"participants": found, "links": links, "gaps": gaps}


def read_export(
    raw,
    project,
    session=None,
    version=None,
    cutoff=None,
    boundary=False,
    project_id=None,
):
    captured_version = getattr(raw, "source_version", None)
    if captured_version:
        if version and version != captured_version:
            raise SourceConflict("version conflict")
        version = captured_version
    data = decode_json(raw, "invalid export JSON")
    if isinstance(data, dict) and "data" in data and "info" not in data:
        data = data["data"]
    if (
        isinstance(data, dict)
        and isinstance(data.get("info"), dict)
        and "location" in data["info"]
    ):
        return read_v2_export(
            data, project, session, version, cutoff, boundary, project_id
        )
    if (
        not isinstance(data, dict)
        or not isinstance(data.get("info"), dict)
        or not isinstance(data.get("messages"), list)
    ):
        raise ReadError("unsupported export schema")
    info = data["info"]
    check_boundary_time(info, cutoff, boundary)
    if version and info.get("version") and version != info["version"]:
        raise SourceConflict("version conflict")
    sid = identifier(info.get("id"), "ses")
    if session is not None and sid != identifier(session, "ses"):
        raise SourceConflict("session mismatch")
    directory = info.get("directory")
    redacted_directory = isinstance(directory, str) and directory.startswith(
        "[redacted:session-directory:"
    )
    if project_id is not None and info.get("projectID") != project_id:
        raise SourceConflict("project ID mismatch")
    if not isinstance(directory, str) or (
        os.path.realpath(directory) != os.path.realpath(project)
        and not (redacted_directory and project_id is not None)
    ):
        raise SourceConflict("project mismatch")
    seen = set()
    for message in data["messages"]:
        if (
            not isinstance(message, dict)
            or not isinstance(message.get("info"), dict)
            or not isinstance(message.get("parts"), list)
        ):
            raise ReadError("unsupported message schema")
        mi = message["info"]
        mid = identifier(mi.get("id"), "msg")
        check_boundary_time(mi, cutoff, boundary)
        if mid in seen:
            raise ReadError("duplicate message")
        seen.add(mid)
        if mi.get("sessionID") != sid:
            raise SourceConflict("message session mismatch")
        for part in message["parts"]:
            if not isinstance(part, dict):
                raise ReadError("unsupported part schema")
            if "state" in part and not isinstance(part["state"], dict):
                raise ReadError("unsupported part state")
            state = part.get("state", {})
            check_boundary_time(part, cutoff, boundary)
            check_boundary_time(state, cutoff, boundary)
            if "metadata" in state and not isinstance(state["metadata"], dict):
                raise ReadError("unsupported part metadata")
            if "time" in state and not isinstance(state["time"], dict):
                raise ReadError("unsupported part time")
            if "time" in part and not isinstance(part["time"], dict):
                raise ReadError("unsupported part time")
            pid = identifier(part.get("id"), "prt")
            if pid in seen:
                raise ReadError("duplicate part")
            seen.add(pid)
            if part.get("sessionID") != sid or part.get("messageID") != mid:
                raise SourceConflict("part identity mismatch")
    fingerprint = hashlib.sha256(
        encode_json(
            {
                "data": data,
                "version": version or info.get("version"),
                "cutoff": cutoff,
                "boundary": boundary,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode()
    ).hexdigest()
    events = []
    for message in data["messages"]:
        mid = message["info"]["id"]
        for obj, kind, ref in [(message["info"], "message", f"{sid}/{mid}")] + [
            (p, p.get("type", "unknown"), f"{sid}/{mid}/{p['id']}")
            for p in message["parts"]
        ]:
            events.append(
                {
                    "ref": ref,
                    "type": kind,
                    "content": encode_json(
                        safe(obj), sort_keys=True, ensure_ascii=True
                    ),
                    "temporal": temporal(obj.get("state", obj), cutoff, boundary),
                }
            )
    return {
        "session": sid,
        "project": os.path.realpath(project),
        "events": events,
        "boundary": boundary,
        "cutoff": cutoff,
        "version": version or info.get("version"),
        "fingerprint": fingerprint,
        "captured_at": int(time.time() * 1000),
        "data": data,
    }


def validate_v2_get(path, query=None):
    if not isinstance(path, str) or not re.fullmatch(
        r"/api/info|/api/session(?:/active|/ses_[A-Za-z0-9]+(?:/message)?)?", path
    ):
        raise ReadError("GET path not allowed")
    allowed = (
        {"directory", "parentID", "limit", "order", "cursor"}
        if path == "/api/session"
        else {"limit", "order", "cursor"}
        if path.endswith("/message")
        else set()
    )
    if any(
        key not in allowed or not isinstance(value, str)
        for key, value in (query or {}).items()
    ):
        raise ReadError("GET query not allowed")


def v2_page_data(get, path, query):
    """Follow body cursors, in source order, with bounded non-repeating pages."""
    rows, seen_cursors, seen_ids = [], set(), set()
    byte_count = 0
    params = dict(query, order="asc", limit="100")
    for _ in range(256):
        page = get(path, params)
        if (
            not isinstance(page, dict)
            or not isinstance(page.get("data"), list)
            or not isinstance(page.get("cursor"), dict)
        ):
            raise ReadError("unsupported V2 page schema")
        for row in page["data"]:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                raise ReadError("unsupported V2 page row")
            if row["id"] in seen_ids:
                raise ReadError("duplicate V2 page row")
            seen_ids.add(row["id"])
            byte_count += len(encode_json(row, ensure_ascii=True).encode())
            if byte_count > MAX_BYTES:
                raise ReadError("source byte limit exceeded; no content processed")
            rows.append(row)
            if len(rows) > 65536:
                raise ReadError("V2 row limit exceeded")
        cursor = page["cursor"].get("next")
        if cursor is None:
            return rows
        if not isinstance(cursor, str) or not cursor or cursor in seen_cursors:
            raise ReadError("invalid V2 pagination cursor")
        seen_cursors.add(cursor)
        params.pop("order", None)
        params["cursor"] = cursor
    raise ReadError("V2 page limit exceeded")


def read_v2_export(data, project, session, version, cutoff, boundary, project_id):
    """Normalize mechanics only; displayed events keep all original V2 fields."""
    info = data["info"]
    sid = identifier(info.get("id"), "ses")
    if session is not None and sid != identifier(session, "ses"):
        raise SourceConflict("session mismatch")
    if version and not v2_version(version):
        raise SourceConflict("version conflict")
    location = info.get("location")
    directory = location.get("directory") if isinstance(location, dict) else None
    redacted = isinstance(directory, str) and directory.lstrip("/").startswith(
        "[redacted:session-directory:"
    )
    if project_id is not None and info.get("projectID") != project_id:
        raise SourceConflict("project ID mismatch")
    if (
        not isinstance(info.get("projectID"), str)
        or not isinstance(directory, str)
        or (
            os.path.realpath(directory) != os.path.realpath(project)
            and not (redacted and project_id is not None)
        )
    ):
        raise SourceConflict("project mismatch")
    if not isinstance(data.get("messages"), list):
        raise ReadError("unsupported V2 export schema")
    check_boundary_time(info, cutoff, boundary)
    messages, events, seen = [], [], set()
    for message in data["messages"]:
        if not isinstance(message, dict) or not isinstance(message.get("type"), str):
            raise ReadError("unsupported V2 message schema")
        mid = identifier(message.get("id"), "msg")
        if mid in seen:
            raise ReadError("duplicate message")
        seen.add(mid)
        check_boundary_time(message, cutoff, boundary)
        content = message.get("content") if message["type"] == "assistant" else []
        if not isinstance(content, list):
            raise ReadError("unsupported V2 assistant content")
        original_info = {
            k: v
            for k, v in message.items()
            if k != "content" or message["type"] != "assistant"
        }
        mi = dict(original_info, sessionID=sid, role=message["type"])
        parts, tool_ids = [], set()
        objects = [(original_info, message["type"], f"{sid}/{mid}", message)]
        for index, part in enumerate(content):
            if not isinstance(part, dict) or not isinstance(part.get("type"), str):
                raise ReadError("unsupported V2 content item")
            check_boundary_time(part, cutoff, boundary)
            p = dict(part, id=f"content/{index}", sessionID=sid, messageID=mid)
            if part["type"] == "tool":
                state = part.get("state")
                if (
                    not isinstance(state, dict)
                    or not isinstance(part.get("name"), str)
                    or not isinstance(part.get("id"), str)
                ):
                    raise ReadError("unsupported V2 tool")
                if state.get("status") not in (
                    "streaming",
                    "running",
                    "completed",
                    "error",
                ):
                    raise ReadError("unsupported V2 tool state")
                if state["status"] == "completed" and (
                    not isinstance(state.get("content"), list) or not state["content"]
                ):
                    raise ReadError("unsupported V2 tool content")
                if part["id"] in tool_ids:
                    raise ReadError("duplicate V2 tool call")
                tool_ids.add(part["id"])
                meta = state.get("metadata", {})
                if not isinstance(meta, dict):
                    raise ReadError("unsupported V2 tool metadata")
                interval = part.get("time", {})
                p["state"] = dict(
                    state,
                    metadata=dict(meta),
                    time={
                        "start": interval.get("ran"),
                        "end": interval.get("completed"),
                    },
                )
                p["tool"] = part["name"]
                if part["name"] == "subagent":
                    p["tool"] = "task"
                    if meta.get("sessionID"):
                        p["state"]["metadata"].update(
                            sessionId=meta["sessionID"], parentSessionId=sid
                        )
            parts.append(p)
            objects.append((part, part["type"], f"{sid}/{mid}/content/{index}", part))
        messages.append({"info": mi, "parts": parts})
        for obj, kind, ref, timing in objects:
            events.append(
                {
                    "ref": ref,
                    "type": kind,
                    "content": encode_json(
                        safe(obj), sort_keys=True, ensure_ascii=True
                    ),
                    "temporal": temporal(timing, cutoff, boundary),
                }
            )
    fingerprint = hashlib.sha256(
        encode_json(
            {"data": data, "version": version, "cutoff": cutoff, "boundary": boundary},
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode()
    ).hexdigest()
    return {
        "session": sid,
        "project": os.path.realpath(project),
        "version": version,
        "fingerprint": fingerprint,
        "captured_at": int(time.time() * 1000),
        "cutoff": cutoff,
        "boundary": boundary,
        "format": "v2",
        "events": events,
        "data": {"info": dict(info, directory=directory), "messages": messages},
    }


def operate(args):
    if args.cutoff is not None and args.cutoff < 0:
        raise ReadError("invalid cutoff")
    if args.captured_boundary and (args.cutoff is None or not args.export_path):
        raise ReadError("captured boundary requires supplied export and cutoff")
    if args.operation == "list":
        if not args.allow_cli:
            raise ReadError("CLI read permission required")
        return {
            "status": "ok",
            "sessions": list_rows(
                cli_capture(
                    args.project,
                    "list",
                    **({"endpoint": args.endpoint} if args.endpoint else {}),
                ),
                args.project,
            ),
            "selected": None,
            "cause": [],
            "remaining": ["Select an exact session before session analysis."],
        }

    def parse(raw, sid=None, boundary=None):
        return read_export(
            raw,
            args.project,
            sid,
            args.version,
            args.cutoff,
            args.captured_boundary if boundary is None else boundary,
            args.project_id,
        )

    v2_cli_stopped = False
    is_v2 = v2_version(args.version)

    def v2_get(path, query=None):
        nonlocal v2_cli_stopped
        if args.allow_cli:
            if v2_cli_stopped:
                raise ReadError("CLI acquisition stopped")
            try:
                raw = cli_capture(
                    args.project, "api", path, endpoint=args.endpoint, query=query
                )
                return decode_json(raw, "invalid API JSON")
            except ReadError:
                v2_cli_stopped = True
                raise
        if args.endpoint:
            return get_json(args.endpoint, args.project, path, query=query)
        raise ReadError("V2 source unavailable")

    def acquire(sid):
        if args.allow_cli:
            if v2_cli_stopped:
                raise ReadError("CLI acquisition stopped")
            raw = cli_capture(
                args.project,
                "export",
                sid,
                **({"endpoint": args.endpoint} if args.endpoint else {}),
            )
            if v2_version(getattr(raw, "source_version", None)):
                server = v2_get("/api/info")
                if not isinstance(server, dict) or not v2_version(
                    server.get("version")
                ):
                    raise ReadError("unsupported server version")
                # In V2 the producer is the server, not the CLI binary.
                raw.source_version = server["version"]
            return parse(raw, sid, boundary=False)
        if args.endpoint:
            if is_v2:
                info = v2_get(f"/api/session/{identifier(sid, 'ses')}")
                if not isinstance(info, dict) or not isinstance(info.get("data"), dict):
                    raise ReadError("unsupported V2 session schema")
                messages = v2_page_data(v2_get, f"/api/session/{sid}/message", {})
                return parse(
                    encode_json({"info": info["data"], "messages": messages}),
                    sid,
                    boundary=False,
                )
            info = get_json(
                args.endpoint, args.project, f"/session/{identifier(sid, 'ses')}"
            )
            messages = get_json(args.endpoint, args.project, f"/session/{sid}/message")
            return parse(
                encode_json({"info": info, "messages": messages}), sid, boundary=False
            )
        raise ReadError("source required; CLI permission or existing endpoint absent")

    root = (
        parse(read_supplied(args.export_path), args.session)
        if args.export_path
        else acquire(identifier(args.session, "ses"))
    )
    sources = {root["session"]: root}
    is_v2 = root.get("format") == "v2"
    v2_online = is_v2 and (args.allow_cli or args.endpoint)
    gaps = []
    children = {}
    statuses = None
    for index, path in enumerate(args.child_export):
        if len(sources) >= 256:
            gaps.append(
                {"kind": "participant-limit", "unprocessed_child_export": index}
            )
            continue
        try:
            child = parse(read_supplied(path))
        except (ReadError, OSError) as error:
            gaps.append(
                {
                    "kind": "child-export-invalid",
                    "child_export_index": index,
                    "failure_status": "conflict"
                    if isinstance(error, SourceConflict)
                    else "error",
                    "reason": str(error)
                    if isinstance(error, SourceConflict)
                    else "invalid or unavailable child export",
                }
            )
            continue
        sid = child["session"]
        if sid in sources and child["fingerprint"] != sources[sid]["fingerprint"]:
            raise ReadError("snapshot conflict in supplied participants")
        sources[sid] = child
    if v2_online:
        try:
            response = v2_get("/api/session/active")
            if not isinstance(response, dict) or not isinstance(
                response.get("data"), dict
            ):
                raise ReadError("unsupported V2 status schema")
            statuses = response["data"]
        except ReadError:
            if args.allow_cli:
                v2_cli_stopped = True
            gaps.append({"kind": "status-unavailable"})
    elif args.endpoint:
        try:
            statuses = get_json(args.endpoint, args.project, "/session/status")
            if not isinstance(statuses, dict):
                raise ReadError("unsupported status schema")
        except ReadError:
            statuses = None
            gaps.append({"kind": "status-unavailable"})
    queue = deque([root["session"]])
    visited = set()
    cli_stopped = False
    while queue:
        sid = queue.popleft()
        if sid in visited:
            continue
        visited.add(sid)
        if len(visited) > 256:
            gaps.append({"kind": "participant-limit", "unprocessed": list(queue)})
            break
        source = sources[sid]
        candidates = set()
        for m in source["data"]["messages"]:
            for part in m["parts"]:
                if part.get("tool") == "task" and part.get("type") == "tool":
                    child = part.get("state", {}).get("metadata", {}).get("sessionId")
                    if child:
                        try:
                            candidates.add(identifier(child, "ses"))
                        except ReadError:
                            gaps.append({"kind": "invalid-task-link", "session": sid})
        if args.endpoint or v2_online:
            try:
                rows = (
                    v2_page_data(v2_get, "/api/session", {"parentID": sid})
                    if is_v2
                    else get_json(
                        args.endpoint, args.project, f"/session/{sid}/children"
                    )
                )
                if not isinstance(rows, list):
                    raise ReadError("unsupported children schema")
                children[sid] = []
                for row in rows:
                    if not isinstance(row, dict):
                        raise ReadError("unsupported children schema")
                    if row.get("parentID") != sid:
                        raise SourceConflict("children parent mismatch")
                    child = identifier(row.get("id"), "ses")
                    children[sid].append(child)
                    candidates.add(child)
            except SourceConflict as error:
                children.pop(sid, None)
                gaps.append(
                    {
                        "kind": "children-GET-conflict",
                        "session": sid,
                        "reason": str(error),
                    }
                )
            except ReadError:
                if is_v2 and args.allow_cli:
                    v2_cli_stopped = True
                children.pop(sid, None)
                gaps.append({"kind": "children-GET-unavailable", "session": sid})
        for child in sorted(candidates):
            if child not in sources:
                if args.allow_cli and cli_stopped:
                    gaps.append({"kind": "cli-acquisition-stopped", "session": child})
                    continue
                if len(sources) >= 256:
                    gaps.append(
                        {"kind": "participant-limit", "unprocessed_session": child}
                    )
                    continue
                try:
                    sources[child] = acquire(child)
                except ReadError as error:
                    if args.allow_cli:
                        cli_stopped = True
                    failure_status = (
                        "conflict"
                        if isinstance(error, SourceConflict)
                        else "error"
                        if args.allow_cli or args.endpoint
                        else "blocked"
                    )
                    gaps.append(
                        {
                            "kind": "child-acquisition-failed",
                            "session": child,
                            "failure_status": failure_status,
                            "reason": str(error)
                            if isinstance(error, SourceConflict)
                            else "source acquisition failed",
                        }
                    )
                    continue
            child_info = sources[child]["data"]["info"]
            if (
                child_info.get("parentID") == sid
                and not child_info.get("fork")
                and child_info.get("projectID")
                == source["data"]["info"].get("projectID")
            ):
                queue.append(child)
    tree = participants(
        root,
        sources,
        args.cutoff,
        args.captured_boundary,
        children if args.endpoint or v2_online else None,
    )
    snapshot_tree = participants(
        root, sources, children=children if args.endpoint or v2_online else None
    )
    late = [
        sid for sid in snapshot_tree["participants"] if sid not in tree["participants"]
    ]
    tree["late_participants"] = late
    gaps.extend(tree["gaps"])
    for sid in sources:
        if sid not in tree["participants"]:
            gaps.append({"kind": "not-in-confirmed-scope", "session": sid})
    for sid in tree["participants"]:
        s = sources[sid]
        if (
            s["data"]["info"]["directory"]
            .lstrip("/")
            .startswith("[redacted:session-directory:")
        ):
            gaps.append(
                {
                    "kind": "redacted-project-directory",
                    "session": sid,
                    "binding": "caller-established project ID",
                }
            )
        if s["version"] not in ("1.18.33", V2_BASELINE):
            gaps.append({"kind": "unverified-version", "session": sid})
        if s.get("format") == "v2":
            gaps.append(
                {
                    "kind": "projected-history",
                    "session": sid,
                    "limitation": "V2 transcript is a projection, not the event log; CLI/supplied exports may omit unsettled assistant, shell and compaction messages",
                }
            )
        for e in s["events"]:
            if e["type"] not in (
                "message",
                "text",
                "reasoning",
                "tool",
                "step-start",
                "step-finish",
                "file",
                "subtask",
                "agent",
                "snapshot",
                "patch",
                "compaction",
                "retry",
                "assistant",
                "user",
                "system",
                "synthetic",
                "skill",
                "shell",
                "agent-switched",
                "model-switched",
                "location-switched",
                "idle",
            ):
                gaps.append({"kind": "unknown-part-type", "ref": e["ref"]})
            if (
                "[redacted:" in e["content"]
                or '"redacted":' in e["content"]
                or '"compacted"' in e["content"]
                or e["type"] == "compaction"
            ):
                gaps.append({"kind": "redacted-pruned-or-compacted", "ref": e["ref"]})
        if args.cutoff is not None:
            gaps.append(
                {
                    "kind": "caller-proven-boundary"
                    if s["boundary"]
                    else "historical-cutoff",
                    "session": sid,
                }
            )
    identity = {
        k: root[k]
        for k in ("session", "project", "version", "fingerprint", "captured_at")
    }
    identity.update(
        updated=root["data"]["info"].get("time", {}).get("updated"),
        cutoff=args.cutoff,
        status=safe(
            statuses.get(root["session"], {"type": "idle"})
            if statuses is not None
            else "unknown"
        ),
        stopped="status describes observation only, not successful completion",
    )
    if args.operation == "overview":
        result = {
            "tree": tree,
            "participants": [
                {
                    "session": sid,
                    "fingerprint": sources[sid]["fingerprint"],
                    "participant_scope": "late snapshot evidence only"
                    if sid in late
                    else "selected historical/snapshot scope",
                    "events": len(sources[sid]["events"]),
                    "content_bytes": sum(
                        len(e["content"]) for e in sources[sid]["events"]
                    ),
                    "last_ref": sources[sid]["events"][-1]["ref"]
                    if sources[sid]["events"]
                    else None,
                    "observed_ranges": [],
                    "unseen": "all indexed content until agent reads pages",
                }
                for sid in tree["participants"] + late
            ],
        }
    elif args.operation == "metrics":
        by_session = [
            metrics(sources[sid], args.cutoff, sources[sid]["boundary"])
            for sid in tree["participants"]
        ]
        result = {
            "participants": by_session,
            "late_snapshot_metrics": [metrics(sources[sid]) for sid in late],
            "late_metrics_scope": "late snapshot only; excluded from all historical totals",
            "time": {
                "unit": "milliseconds",
                "assistant_elapsed_union": union(
                    [
                        span
                        for m in by_session
                        for span in m["time"]["assistant_intervals"]
                    ]
                ),
                "tool_union_excluding_parent_task_wait": union(
                    [span for m in by_session for span in m["time"]["tool_intervals"]]
                ),
                "limitations": "category unions overlap; no inferred thinking, generation or human wait",
            },
        }
    else:
        sid = args.participant or root["session"]
        if sid not in tree["participants"] + late:
            raise ReadError("participant outside confirmed scope")
        source = sources[sid]
        if args.operation == "detail":
            matches = [e for e in source["events"] if e["ref"] == args.ref]
            if len(matches) != 1:
                raise ReadError("detail ref not found")
            source = dict(source, events=matches, view=args.ref)
        cursor = (
            decode_json(args.cursor, "invalid cursor JSON") if args.cursor else None
        )
        result = pages(source, cursor, args.budget)
        result["participant_scope"] = (
            "late snapshot evidence only"
            if sid in late
            else "selected historical/snapshot scope"
        )
    # Coverage limitations do not themselves fail a bounded read. Required
    # acquisitions and contradictory participant links do; retain the payload
    # and exact gaps so consumers can recover without replaying successful reads.
    failures = {
        "child-export-invalid": "error",
        "status-unavailable": "error",
        "children-GET-conflict": "conflict",
        "participant-limit": "blocked",
        "child-acquisition-failed": "blocked",
        "cli-acquisition-stopped": "blocked",
        "missing-task-link": "blocked",
        "invalid-task-link": "conflict",
        "missing-child": "blocked",
        "foreign-parent": "conflict",
        "foreign-project": "conflict",
        "reused-or-cycle": "conflict",
    }
    cause = [g for g in gaps if g["kind"] in failures]
    statuses = {g.get("failure_status", failures[g["kind"]]) for g in cause}
    status = next((s for s in ("conflict", "error", "blocked") if s in statuses), "ok")
    remaining = [
        f"Resolve {g['kind']}: {encode_json(g, sort_keys=True)} using supplied evidence or permitted reads; retain verified sources."
        for g in cause
    ]
    if args.operation in ("overview", "metrics"):
        remaining.append(
            "Read indexed content pages before claiming session analysis coverage."
        )
    elif result["next"] is not None:
        remaining.append(
            "Continue returned fingerprint-bound next cursor for unread content."
        )
    return {
        "status": status,
        "identity": identity,
        "gaps": gaps,
        "result": result,
        "cause": cause,
        "remaining": remaining,
    }


def read_supplied(path):
    if path == "-":
        raw = sys.stdin.read(MAX_BYTES + 1)
    else:
        with open(path, "rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ReadError("source byte limit exceeded; no content processed")
    return raw


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "operation", choices=["list", "overview", "pages", "detail", "metrics"]
    )
    p.add_argument("--project", required=True)
    p.add_argument(
        "--project-id",
        help="independently established exact project ID, required for erased directory",
    )
    p.add_argument("--session")
    p.add_argument("--export", dest="export_path", help="supplied file or - for stdin")
    p.add_argument("--child-export", action="append", default=[])
    p.add_argument("--version", help="explicitly established source semantic version")
    p.add_argument("--endpoint", help="explicit authorized already available endpoint")
    p.add_argument(
        "--allow-cli",
        action="store_true",
        help="authorize fixed CLI reads (V2 authenticated service client; V1 --pure); accepts ordinary service effects, not a storage-fitness assertion",
    )
    p.add_argument("--cutoff", type=int, help="Unix milliseconds")
    p.add_argument(
        "--captured-boundary",
        action="store_true",
        help="caller has evidence this export was captured at cutoff",
    )
    p.add_argument("--participant", help="exact participant for pages/detail")
    p.add_argument("--cursor", help="fingerprint-bound JSON continuation")
    p.add_argument("--budget", type=int, default=8192)
    p.add_argument("--ref", help="exact session/message[/part] address for detail")
    return p


def main():
    try:
        result = operate(parser().parse_args())
        print(encode_json(result, ensure_ascii=True))
        return 0
    except ReadError as error:
        print(json.dumps({"status": "error", "diagnostic": str(error)}))
        return 2
    except RecursionError:
        print(
            json.dumps({"status": "error", "diagnostic": "JSON nesting limit exceeded"})
        )
        return 2
    except (OSError, ValueError, TypeError, KeyError):
        print(
            json.dumps(
                {"status": "error", "diagnostic": "unavailable or unsupported source"}
            )
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())
