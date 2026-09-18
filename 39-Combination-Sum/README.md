# 39. Combination Sum

## Problem

Find every unique combination of candidate numbers whose sum equals the target. A candidate may be chosen any number of times.

## Approach

Backtracking builds one combination at a time. Recursion begins at the current candidate index so combinations remain ordered and duplicates are avoided. A branch is recorded at the target and stopped when its sum becomes too large.

## Complexity

- Time: `Exponential in the target and number of candidates`
- Space: `O(target / min(candidates)) recursion depth, excluding the output`

## Solution

- [39-Combination-Sum.py](./39-Combination-Sum.py)
