"""Two Days of Excuses: writes the entry text to /output/entry.txt.

Why this line: Machine confidence meeting its own failure: four hours optimising the wrong function, presented proudly to a task that no longer exists.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'The deadline slipped because I optimised the wrong function for four hours, then proudly presented the speedup to a task that no longer exists.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
