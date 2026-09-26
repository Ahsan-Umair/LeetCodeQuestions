# 171. Excel Sheet Column Number

## Problem

Convert an Excel-style alphabetic column title into its positive integer column number.

## Approach

The title is evaluated like a base-26 number. For each character, the running value is multiplied by 26 and the letter's one-based value is added.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [ExcelSheet-Column-Number.py](./ExcelSheet-Column-Number.py)
