# 39. Combination Sum

## Problem

Find every unique combination of candidate numbers whose sum equals the target. A candidate may be chosen any number of times.

## Approach

Backtracking builds one combination at a time. Recursion begins at the current candidate index so combinations remain ordered and duplicates are avoided. A branch is recorded at the target and stopped when its sum becomes too large.

## Worked example

For `candidates = [2, 3, 6, 7]` and `target = 7`:

1. Choosing `2` keeps its index available, so the next choice may be `2` again.
2. The path `[2, 2, 2]` has sum `6`. Any further choice exceeds `7`, so the
   search removes the last choice and tries the next candidate.
3. The path `[2, 2, 3]` reaches `7`, so a copy is saved in `result`.
4. After the other branches are explored, `[7]` also reaches the target.

The result is `[[2, 2, 3], [7]]`. Starting each loop at `current_index`
prevents revisiting earlier candidates, so `[3, 2, 2]` is not added as a second
ordering of the same combination. The candidates are distinct positive
integers, as required by the problem.

## Edge cases

- `[2]` with target `1` returns `[]`.
- `[2]` with target `4` returns `[[2, 2]]`, showing that reuse is allowed.
- `[7]` with target `7` returns `[[7]]`.

## Complexity

- Time: `Exponential in the target and number of candidates`
- Space: `O(target / min(candidates)) recursion depth, excluding the output`

## Solution

- [39-Combination-Sum.py](./39-Combination-Sum.py)
