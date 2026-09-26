# 3483. Unique 3-Digit Even Numbers

## Problem

Using the supplied digits at most once per position, count the distinct three-digit even numbers that can be formed without a leading zero.

## Approach

Three nested loops choose distinct indices for the hundreds, tens, and units digits. The first digit is required to be nonzero and the last digit even. Valid numbers are inserted into a set so duplicate digit combinations count only once.

## Complexity

- Time: `O(m³), where `m` is the number of supplied digits`
- Space: `O(u), where `u` is the number of unique valid numbers`

## Solution

- [3483-Unique-3-Digits-Even-Numbers.py](./3483-Unique-3-Digits-Even-Numbers.py)
