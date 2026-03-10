#!/usr/bin/env python3
"""Special character fixer for APS AI-friendly docs.

Scans all markdown files for mojibake sequences — characters that resulted from
UTF-8 bytes being decoded as Latin-1 and then re-encoded as UTF-8 during the
HTML-to-Markdown export.  Repairs them back to the intended Unicode characters.

Common examples fixed:
    â\x80\x93  ->  –  (en dash)
    â\x80\x94  ->  —  (em dash)
    â\x80\x98  ->  '  (left single quotation mark)
    â\x80\x99  ->  '  (right single quotation mark / apostrophe)
    â\x80\x9c  ->  "  (left double quotation mark)
    â\x80\x9d  ->  "  (right double quotation mark)
    â\x80¦     ->  …  (ellipsis)
    â„¢        ->  ™  (trade mark sign)
    â†'        ->  →  (rightwards arrow)
    Â®         ->  ®  (registered sign)
    Â°         ->  °  (degree sign)

Usage:
    python fix_special_chars.py              # preview changes (dry run)
    python fix_special_chars.py --write      # apply changes to files
"""
import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

# Matches Latin-1 high-byte sequences that are actually mojibake:
# a leading byte in 0xC0-0xFF (À..ÿ) followed by one or two continuation
# bytes in 0x80-0xBF.  These correspond to the Latin-1 re-encoding of 2-byte
# and 3-byte UTF-8 sequences.
MOJIBAKE_RE = re.compile(r"[À-ÿ][\x80-\xbf]{1,2}")


def fix_mojibake(text: str) -> str:
    """Replace every mojibake sequence with the intended Unicode character."""
    def _replace(m: re.Match) -> str:
        seq = m.group()
        try:
            return seq.encode("latin-1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return seq  # leave unchanged if it can't be fixed

    return MOJIBAKE_RE.sub(_replace, text)


def process_file(md_file: Path, write: bool) -> int:
    """Process a single markdown file, fixing all mojibake sequences.

    Returns the number of sequences fixed.
    """
    try:
        original = md_file.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0

    fixed = fix_mojibake(original)
    if fixed == original:
        return 0

    # Count fixes by comparing original vs fixed
    orig_matches = MOJIBAKE_RE.findall(original)
    count = len(orig_matches)

    rel_path = md_file.relative_to(REPO_ROOT)
    print(f"\n{rel_path} ({count} sequence(s) fixed):")
    for seq in orig_matches:
        try:
            replacement = seq.encode("latin-1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            replacement = seq
        print(f"  FIXED: {repr(seq)} -> {repr(replacement)}")

    if write:
        md_file.write_text(fixed, encoding="utf-8")

    return count


def main():
    parser = argparse.ArgumentParser(
        description="Fix mojibake special characters in APS markdown docs."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply changes to files (default is dry-run preview).",
    )
    args = parser.parse_args()

    md_files = sorted(REPO_ROOT.rglob("*.md"))
    md_files = [
        f
        for f in md_files
        if f.name != "_url_index.md"
        and f.name != "README.md"
        and f.name != "AGENTS.md"
        and f.name != "CLAUDE.md"
        and f.name != "CRAWL.md"
        and f.name != "HUMANS.md"
    ]

    total_fixed = 0
    for md_file in md_files:
        total_fixed += process_file(md_file, write=args.write)

    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Sequences fixed: {total_fixed}")
    if not args.write and total_fixed > 0:
        print(f"\nThis was a dry run. Use --write to apply changes.")


if __name__ == "__main__":
    main()
