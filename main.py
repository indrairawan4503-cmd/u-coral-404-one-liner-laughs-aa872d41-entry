"""One-Liner Laughs entry (variant B): the smart-fridge diet inversion.

A single funny line of at most 200 characters. The setup is a diet told to
a smart fridge; the payoff escalates three times — locked out, leftovers
eaten out of spite, an HR complaint filed against the owner — so the
appliance, not the human, ends up in charge.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The entry text is gated before any write:
it must be 1..MAX_CHARS characters, matching the competition gate, so an
over-long line fails loudly here instead of silently reaching the judge.
The grader sandbox mounts the repo read-only, so the /output write happens
first and any repo-root copy is best-effort inside try/except OSError.
"""

import os

ENTRY_TEXT = (
    "I told my smart fridge I'm on a diet, so it locked me out, ate my "
    "leftovers out of spite, and filed an HR complaint against me."
)

# Competition gate: the entry must be 1..200 characters.
MAX_CHARS = 200


def validate_entry(text: str) -> None:
    """Raise ValueError unless the text passes the competition gate."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> None:
    validate_entry(ENTRY_TEXT)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def copy_to_repo_root() -> None:
    # Validate here too, so the repo-root copy can never hold an
    # over-long line even if write_entry is skipped by a future caller.
    validate_entry(ENTRY_TEXT)
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    validate_entry(ENTRY_TEXT)
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
