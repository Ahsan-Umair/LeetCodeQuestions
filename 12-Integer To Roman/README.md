# 12. Integer to Roman

## Problem

Convert an integer into its Roman numeral representation.

## Approach

The solution processes Roman numeral values from largest to smallest, including
the subtractive pairs `CM`, `CD`, `XC`, `XL`, `IX`, and `IV`. While the
remaining number is at least the current value, its symbol is appended and the
value is subtracted. Processing denominations in descending order produces the
canonical Roman numeral.

## Complexity

- Time: `O(n)` where `n` is the number of symbols in the result
- Space: `O(n)` for the result

## Solution

- [12-Integer-To-Roman.py](./12-Integer-To-Roman.py)
