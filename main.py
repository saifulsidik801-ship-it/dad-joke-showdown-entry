#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun).

Writes exactly one dad joke, at most 200 characters, to /output/entry.txt.

Joke selection: ten candidates were drafted and weighed against the judge's
brief -- pun lands cleanly on first read, feels fresh, tight with the
punchline at the end, reads naturally aloud. The winner below beat the
runner-ups ("That's a whisk I'm willing to take", "I only deal with current
relationships", "In case I need to draw the line somewhere"): its setup
sounds like a threat, the son's reaction sells the misdirection, and the
last line reframes it as an innocent calendar -- the biggest groan of the
shortlist, and not a joke told a thousand times.
"""

import os

JOKE = "I told my son his days are numbered. He said, 'Dad, that's dark.' I said, 'No, that's a calendar.'"


def main() -> None:
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(joke)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
