# 561. Array Partition

## Problem

Split `2n` integers into pairs so that the sum of the smaller value from every pair is as large as possible.

## Approach

After sorting the array, adjacent values form optimal pairs. The solution takes every value at an even index—the smaller member of each sorted pair—and sums them.

## Complexity

- Time: `O(n log n)`
- Space: `O(n) for the collected values, in addition to the in-place sort`

## Solution

- [561-Array-Partition.py](./561-Array-Partition.py)
