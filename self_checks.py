"""Student-facing self-checks for Tutorial 5 (same cases as the autograder)."""
from __future__ import annotations

import copy


def _same(got, expected, tol=None):
    if tol is None:
        return got == expected
    try:
        return abs(got - expected) <= tol
    except TypeError:
        return False


def _run_groups(func, func_name, groups):
    earned = total = 0
    for title, points, cases in groups:
        problems = []
        for args, expected, tol, hint in cases:
            call = f"{func_name}({', '.join(repr(a) for a in args)})"
            try:
                got = func(*copy.deepcopy(args))
            except Exception as e:
                problems.append(
                    f"    Case failed: {call}\n    Raised {type(e).__name__}: {e}"
                )
                continue
            if not _same(got, expected, tol):
                msg = (
                    f"    Case failed: {call}\n"
                    f"    Expected: {expected!r}\n"
                    f"    Got:      {got!r}"
                )
                if hint:
                    msg += f"\n    Hint:     {hint}"
                problems.append(msg)
        total += points
        if problems:
            print(f"[FAIL] {title}  (0/{points} pt)")
            print("\n".join(problems))
        else:
            earned += points
            print(f"[PASS] {title}  ({points}/{points} pt)")
    print(f"\nSelf-check score: {earned}/{total}")
    return earned == total


BUILD_HISTOGRAM_GROUPS = [
    (
        "build_histogram: basic frequencies",
        1,
        [
            (
                ([1, 2, 2, 3, 3, 3, 4],),
                {1: 1, 2: 2, 3: 3, 4: 1},
                None,
                "count how many times each value appears",
            ),
        ],
    ),
    (
        "build_histogram: empty list",
        1,
        [
            (([],), {}, None, "empty input -> empty dict"),
        ],
    ),
    (
        "build_histogram: all identical",
        1,
        [
            (([7, 7, 7, 7],), {7: 4}, None, "one key with count = length"),
        ],
    ),
    (
        "build_histogram: strings",
        1,
        [
            (
                (["a", "b", "a", "c", "b", "a"],),
                {"a": 3, "b": 2, "c": 1},
                None,
                "works for any hashable values, not only ints",
            ),
        ],
    ),
    (
        "build_histogram: mixed ints",
        1,
        [
            (
                ([0, -1, 0, 2, -1, 2, 2],),
                {0: 2, -1: 2, 2: 3},
                None,
                "zeros and negatives are valid keys",
            ),
        ],
    ),
]


def run_build_histogram_checks(func):
    """Run build_histogram self-checks. Pass the function object."""
    return _run_groups(func, "build_histogram", BUILD_HISTOGRAM_GROUPS)
