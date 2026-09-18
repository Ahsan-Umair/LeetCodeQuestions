# 349. Intersection of Two Arrays — Nested Loops

## Problem

Return the distinct values that appear in both input arrays.

## Approach

The solution compares every value in the first array with every value in the second. Matching values are added only if they are not already present in the result list.

## Complexity

- Time: `O(n × m × u) in the worst case because duplicate suppression searches the result list`
- Space: `O(u), where `u` is the number of distinct common values`

## Solution

- [349-Intersection-of-Two-Arrays-Method # 1.py](./349-Intersection-of-Two-Arrays-Method%20%23%201.py)
