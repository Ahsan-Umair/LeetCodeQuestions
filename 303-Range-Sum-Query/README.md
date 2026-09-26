# 303. Range Sum Query — Immutable

## Problem

Store an integer array and answer repeated queries for the sum of elements between two inclusive indices.

## Approach

The constructor builds a prefix-sum array with a leading zero. Each query subtracts `prefix[left]` from `prefix[right + 1]`, so the requested range sum is returned without scanning the range again.

## Complexity

- Time: `O(n) preprocessing and O(1) per query`
- Space: `O(n)`

## Solution

- [303-Range-Sum-Query.py](./303-Range-Sum-Query.py)
