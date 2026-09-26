# 268. Missing Number

## Problem

An array contains distinct numbers from `0` through `n` with one value missing. Return the missing value.

## Approach

The expected sum of `0...n` is computed with the arithmetic-series formula. Subtracting the actual array sum leaves the missing number.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [268-MissingNumber.py](./268-MissingNumber.py)
