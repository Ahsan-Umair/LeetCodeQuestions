# 88. Merge Sorted Array

## Problem

Merge two sorted arrays into `nums1`, which has enough trailing space to hold all values.

## Approach

Three pointers work from right to left: one at each array's last valid element and one at the final write position. The larger remaining value is written first, preventing unread values in `nums1` from being overwritten.

## Complexity

- Time: `O(m + n)`
- Space: `O(1)`

## Solution

- [Merge-Sorted-Array.py](./Merge-Sorted-Array.py)
