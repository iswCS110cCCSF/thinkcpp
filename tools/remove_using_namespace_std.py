from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "pretext"

# These replacements are intentionally conservative.
# Longer and more specific names should appear before shorter names.
STD_NAMES = [
    "unordered_multimap",
    "unordered_multiset",
    "unordered_map",
    "unordered_set",
    "multimap",
    "multiset",
    "stringstream",
    "istringstream",
    "ostringstream",
    "ifstream",
    "ofstream",
    "fstream",
    "numeric_limits",
    "runtime_error",
    "invalid_argument",
    "out_of_range",
    "length_error",
    "logic_error",
    "exception",
    "make_pair",
    "make_unique",
    "make_shared",
    "unique_ptr",
    "shared_ptr",
    "weak_ptr",
    "lower_bound",
    "upper_bound",
    "binary_search",
    "stable_sort",
    "reverse",
    "accumulate",
    "transform",
    "remove_if",
    "find_if",
    "getline",
    "string",
    "vector",
    "array",
    "deque",
    "list",
    "forward_list",
    "map",
    "set",
    "pair",
    "tuple",
    "queue",
    "priority_queue",
    "stack",
    "iterator",
    "cout",
    "cin",
    "cerr",
    "clog",
    "endl",
    "flush",
    "fixed",
    "scientific",
    "setprecision",
    "setw",
    "left",
    "right",
    "boolalpha",
    "noboolalpha",
    "sort",
    "swap",
    "min",
    "max",
    "abs",
    "sqrt",
    "pow",
]

USING_NAMESPACE_RE = re.compile(
    r"^[ \t]*using[ \t]+namespace[ \t]+std[ \t]*;[ \t]*(?:\r?\n)?",
    re.MULTILINE,
)

# PreTeXt code elements commonly used for programs.
CODE_BLOCK_RE = re.compile(
    r"(?P<open><program\b[^>]*>)"
    r"(?P<body>.*?)"
    r"(?P<close></program>)",
    re.DOTALL | re.IGNORECASE,
)


def qualify_std_names(code: str) -> str:
    code = USING_NAMESPACE_RE.sub("", code)

    for name in STD_NAMES:
        pattern = re.compile(
            rf"(?<![\w:]){re.escape(name)}(?![\w])"
        )

        def replacement(match: re.Match[str]) -> str:
            start = match.start()

            # Do not modify preprocessor lines such as #include.
            line_start = code.rfind("\n", 0, start) + 1
            line_prefix = code[line_start:start]
            if line_prefix.lstrip().startswith("#"):
                return match.group(0)

            return f"std::{match.group(0)}"

        code = pattern.sub(replacement, code)

    # Repair accidental double qualification.
    code = code.replace("std::std::", "std::")
    return code


def transform_file(text: str) -> str:
    def transform_block(match: re.Match[str]) -> str:
        body = match.group("body")

        # Only touch blocks that actually use the namespace directive.
        if not re.search(r"\busing\s+namespace\s+std\s*;", body):
            return match.group(0)

        new_body = qualify_std_names(body)
        return f"{match.group('open')}{new_body}{match.group('close')}"

    return CODE_BLOCK_RE.sub(transform_block, text)


def process_file(path: Path, write: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = transform_file(original)

    if updated == original:
        return False

    relative = path.relative_to(ROOT)
    print(f"\n--- {relative}")

    diff = difflib.unified_diff(
        original.splitlines(),
        updated.splitlines(),
        fromfile=f"a/{relative}",
        tofile=f"b/{relative}",
        lineterm="",
    )
    print("\n".join(diff))

    if write:
        path.write_text(updated, encoding="utf-8", newline="\n")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove 'using namespace std;' from C++ code blocks."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes. Without this option, only show a dry-run diff.",
    )
    args = parser.parse_args()

    changed = 0

    for path in sorted(SOURCE_ROOT.rglob("*.ptx")):
        if process_file(path, args.write):
            changed += 1

    mode = "updated" if args.write else "would update"
    print(f"\n{changed} file(s) {mode}.")


if __name__ == "__main__":
    main()