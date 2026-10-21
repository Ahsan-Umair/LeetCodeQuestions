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

## Complexity

- Time: `O(2^n)` in the worst case, excluding the cost of copying results
- Space: `O(n)` auxiliary recursion and path space, excluding the output

## Solution

- [40-Combination-Sum-II.py](./40-Combination-Sum-II.py)
