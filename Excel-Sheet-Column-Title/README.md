# 168. Excel Sheet Column Title

## Problem

Convert a positive column number into its corresponding Excel-style alphabetic column title.

## Approach

The number is treated as a one-indexed base-26 value. Subtracting one before each modulo operation maps remainders to `A...Z`; the quotient is processed until it reaches zero.

## Complexity

- Time: `O(log₂₆ n)`
- Space: `O(log₂₆ n) for the output`

## Solution

- [Excel-Sheet-Column-Title.py](./Excel-Sheet-Column-Title.py)
