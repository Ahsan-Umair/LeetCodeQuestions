# 13. Roman to Integer

## Problem

Convert a valid Roman numeral string into its integer value.

## Approach

A dictionary maps symbols to values. A symbol is subtracted when it is smaller than the following symbol, which handles subtractive pairs; otherwise, it is added.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Roman-To-Integer.py](./Roman-To-Integer.py)
