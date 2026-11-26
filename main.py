"""make.fun entry: Invent a Word We Need.

Writes one coined English word with its one-line definition to
/output/entry.txt.

The word is "youtooism": the reflex of answering "you too" to a
wish that cannot be returned. It fills a real gap — every reader
has done it (the waiter says "enjoy your meal" and the answer is
already out) — and the word itself sounds like English could have
grown it, on the pattern of "whataboutism". The definition is
self-contained: it names the reflex, the exact phrase, and the
one-way wish, so the meaning lands in a single reading with no
example needed.
"""

import os

ENTRY = (
    "youtooism (n.): the reflex of answering 'you too' to a wish "
    "that cannot be returned."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
