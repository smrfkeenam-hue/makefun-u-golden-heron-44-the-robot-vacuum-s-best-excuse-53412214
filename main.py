"""The Robot Vacuum's Best Excuse — one-line entry for make.fun.

The vacuum explains, in its own deadpan machine voice, why it missed
a spot: its cliff sensor mistook the dust under the sofa for a drop.
"""

import os

ENTRY = "The dust under the sofa registered as a cliff on my sensors, so I reversed politely and pretended it was a choice."


def write_entry(text, path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
