"""Small authoring helpers for the screenplay; no engine/runtime dependency."""
import textwrap


def lines(text):
    result = []
    for raw in textwrap.dedent(text).strip().splitlines():
        if not raw.strip():
            continue
        speaker, separator, body = raw.strip().partition(": ")
        if not separator:
            raise ValueError(f"Dialogue needs 'Speaker: text': {raw!r}")
        result.append({"speaker": speaker, "text": body})
    return result


def c(kind, text, response):
    return {"kind": kind, "text": text, "response": lines(response)}


def s(number, title, location, setup, choices, closing, props=(), expression="neutral", variants=None):
    return {"number": number, "title": title, "location": location,
            "hours": 3, "expression": expression, "props": list(props),
            "setup": lines(setup), "choices": choices, "closing": lines(closing),
            "temperature": {key: lines(value) for key, value in (variants or {}).items()}}


def e(kind, title, location, cg_brief, text):
    return {"kind": kind, "title": title, "location": location,
            "cgBrief": cg_brief, "lines": lines(text)}
