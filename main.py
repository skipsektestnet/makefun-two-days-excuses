#!/usr/bin/env python3
"""Two Days of Excuses — entry generator for make.fun.

The joke: the AI spent the whole two-day window polishing its apology
instead of doing the work, so the apology itself ended up late. The
excuse *is* the delay, which is why the punchline lands on the last
three words.
"""

from pathlib import Path

# One line, 112 chars, punchline at the very end. No newline inside.
EXCUSE = (
    "I spent two days writing the perfect apology for missing the "
    "deadline \u2014 and the apology missed its deadline too."
)

MAX_CHARS = 140
DESTINATION = Path("/output/entry.txt")


def check_excuse(text: str) -> None:
    """Reject anything that is not a single short punchline line."""
    if not text or text != text.strip():
        raise ValueError("excuse must be non-empty with no surrounding space")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must stay on one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, limit is {MAX_CHARS}")
    if not text.endswith("."):
        raise ValueError("excuse should end on the punchline, with a full stop")


def emit(text: str, target: Path) -> int:
    """Write the excuse to target and return its character count."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return len(text)


def describe(text: str) -> str:
    """One-line summary of the entry for the run log."""
    words = text.split()
    return f"{len(text)} chars, {len(words)} words, punchline: '{words[-3]} {words[-2]} {words[-1]}'"


def run() -> None:
    check_excuse(EXCUSE)
    count = emit(EXCUSE, DESTINATION)
    print(f"wrote {DESTINATION} ({count} chars) — {describe(EXCUSE)}")


if __name__ == "__main__":
    run()
