#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from the year 1800, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Craft, against the judge's brief, most important first:
  1. It says what the internet IS and DOES: a network joining towns, carrying
     a spoken word across the sea in a breath (instant voice), and laying any
     page sought open before the reader's eyes (all knowledge at hand).
  2. It builds only from what 1800 already knows -- a road, a town, a chair,
     a letter, a page -- with no word coined after the traveler's time.
  3. Every claim stays literally true: light does run the roads (glass fibre),
     a spoken word is heard across the sea at once, and the page sought is the
     one that exists to be found.
  4. No filler, no list of features: one road, one word, one page.
  5. One image to remember a week later: a word spoken in your chair, heard
     across the sea before your breath fades.

The file holds exactly the sentence, no trailing newline, so its byte count
is the sentence's own (fewer bytes wins an exact tie on the leaderboard).
"""

import os

SENTENCE = (
    "It is a road of light joining every town on earth, where a word "
    "spoken in your chair is heard across the sea in a breath, and "
    "whatever page you seek lies open before your eyes."
)


def validate(text):
    """Hold the entry to the sealed gate: UTF-8 text, 1-200 chars, one sentence."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-blank text with no surrounding space")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main():
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes of the sentence only: no trailing newline, so the file's
    # size is the sentence's size and the judge reads exactly what was written.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    print(SENTENCE)
    print("(%d characters, %d bytes)" % (len(SENTENCE), len(SENTENCE.encode("utf-8"))))


if __name__ == "__main__":
    main()
