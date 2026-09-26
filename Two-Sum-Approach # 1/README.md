# 1. Two Sum — Brute Force

## Problem

Return the indices of two distinct array elements whose sum equals the target.

## Approach

The intended brute-force approach uses nested loops to test every pair, starting the inner loop immediately after the outer index so an element is never paired with itself. The first matching pair is returned.

## Complexity

- Time: `O(n²)`
- Space: `O(1)`

## Solution

- [Two-Sum-Approach # 1.py](./Two-Sum-Approach%20%23%201.py)
