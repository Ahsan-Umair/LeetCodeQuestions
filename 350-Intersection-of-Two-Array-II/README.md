# 350. Intersection of Two Arrays II

## Problem

Return the intersection of two arrays while preserving the number of times each common value occurs.

## Approach

A dictionary counts occurrences in the first array. The second array is scanned, and a value is appended whenever its stored count is still positive; that count is then decremented.

## Complexity

- Time: `O(n + m)`
- Space: `O(n)`

## Solution

- [350-Intersection-of-Two-Array-II.py](./350-Intersection-of-Two-Array-II.py)
