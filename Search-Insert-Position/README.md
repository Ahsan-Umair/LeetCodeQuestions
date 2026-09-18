# 35. Search Insert Position

## Problem

In a sorted array, return the index of a target or the index where it should be inserted to preserve order.

## Approach

Binary search narrows the inclusive search range. If the target is absent, `left` finishes at the first position containing a larger value, which is exactly the insertion index.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Solution

- [Search-Insert-Position.py](./Search-Insert-Position.py)
