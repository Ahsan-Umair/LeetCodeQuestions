# 66. Plus One

## Problem

Treat an array of decimal digits as a nonnegative integer, add one, and return the resulting digits.

## Approach

The solution scans from right to left. A digit below nine is incremented and returned immediately; a nine becomes zero and carries to the next position. If the leading digit also carries, a new `1` is inserted at the front.

## Complexity

- Time: `O(n)`
- Space: `O(1) auxiliary space, excluding possible growth of the output array`

## Solution

- [Plus-One.py](./Plus-One.py)
