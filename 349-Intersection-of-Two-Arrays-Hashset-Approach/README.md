# 349. Intersection of Two Arrays — Hash Set

## Problem

Return the distinct values that appear in both input arrays.

## Approach

The first array is converted to a set. While scanning the second array, a value found in the set is appended to the result and removed from the set, which prevents duplicate output.

## Complexity

- Time: `O(n + m) on average`
- Space: `O(n)`

## Solution

- [349-Intersection-of-Two-Arrays-Hashset-Approach.py](./349-Intersection-of-Two-Arrays-Hashset-Approach.py)
