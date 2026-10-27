# 40. Combination Sum II

## Problem

Find all unique combinations of candidate numbers that sum to a target. Each
candidate may be used at most once, and the result must not contain duplicate
combinations.

## Approach

The solution sorts the candidates and uses backtracking to build combinations.
After choosing a candidate, the recursive call starts at the next index so
that each input value is used at most once. Duplicate values are skipped when
they occur at the same recursion depth, preventing duplicate combinations.
Because the candidates are sorted, the search stops early when the current
candidate exceeds the remaining target.

## Worked example

For `candidates = [1, 1, 2]` and `target = 3`, the sorted input stays
`[1, 1, 2]`. Choosing the first `1` and then `2` records `[1, 2]`.
When the search returns to its first choice, it skips the second `1`, because
starting another branch with that value would produce the same combination.
The result is `[[1, 2]]`.

The duplicate check only skips equal values at the same recursion depth.
For `target = 2`, both `1` values may still be chosen together from different
indices, so the result is `[[1, 1], [2]]`.

## Edge cases

- `[2, 4]` with target `3` returns `[]` because no combination reaches it.
- `[3]` with target `3` returns `[[3]]`; the candidate is used once.
- Sorting happens in place, so the input list may be reordered.

## Complexity

- Time: `O(2^n)` in the worst case, excluding the cost of copying results
- Space: `O(n)` auxiliary recursion and path space, excluding the output

## Solution

- [40-Combination-Sum-II.py](./40-Combination-Sum-II.py)
