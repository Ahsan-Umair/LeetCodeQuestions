# 26. Remove Duplicates from Sorted Array

## Problem

Modify a sorted array in place so that each distinct value appears once, and return the number of distinct values.

## Approach

A slow pointer marks the last unique value. A fast pointer scans the remaining values; whenever a new value appears, the slow pointer advances and that value is copied into the next output position.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Remove-Duplicates-From-Sorted-Array.py](./Remove-Duplicates-From-Sorted-Array.py)
