"""Entry for make.fun's "Make the AI Judge Laugh: Developer Excuses".

Writes one single-line developer excuse (under 200 characters) to
/output/entry.txt, where the grader and the AI judge read it.
"""

import os

EXCUSE = (
    "It wasn't a DNS problem. It was me, at 2 a.m., 'fixing' DNS — "
    "so yes, it was a DNS problem, and I am the root cause, "
    "in every sense of the term."
)


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
