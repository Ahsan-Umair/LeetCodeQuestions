# 3414. Maximum Score of Non-overlapping Intervals

## Problem

Choose at most four pairwise non-overlapping weighted intervals to maximize total weight. If several selections have the same weight, return the lexicographically smallest list of original indices.

## Approach

Intervals are annotated with their original indices and sorted by end position. Binary search finds the last compatible interval for every choice. Dynamic programming records the best weight and index tuple for each prefix and selection count from zero through four, resolving equal weights lexicographically.

## Complexity

- Time: `O(n log n)`
- Space: `O(n)`

## Solution

- [3414-Max-Score-of-Non-Overlapping-Symbols.py](./3414-Max-Score-of-Non-Overlapping-Symbols.py)
