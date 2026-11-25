"""charm-the-commuter-forecast: one line of weather for a city that isn't.

Gloomborough does not exist, but its rain does. The line opens like a
real broadcast forecast — city named first, weather the whole point —
then bends the register: "rain with ambition" is the forecast's own
rhythm turned into a joke, and the twist lands in the last words, aimed
straight at the bored commuter at the rainy bus stop: the pigeons have
umbrellas, and you don't. One concrete, surprising image; every word
earns its place.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "Gloomborough: rain until noon, then rain with ambition — the 7:40 bus is 20 minutes late, the pigeons have umbrellas, and you don't."

MAX_CHARS = 140


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    text = entry_text()
    out.write_text(text, encoding="utf-8")
    # Read it back and refuse a write that did not land byte for byte.
    if out.read_text(encoding="utf-8") != text:
        raise RuntimeError("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
