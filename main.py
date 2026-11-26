"""Pigeon Pitch, One Line.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt.
"""

import os

ENTRY = (
    "We've built a subscription service that delivers breadcrumbs "
    "before you drop them - four billion crumbs a day, zero churn, "
    "and our users physically cannot leave the park."
)


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text of 1-200 characters, not only whitespace."""
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
