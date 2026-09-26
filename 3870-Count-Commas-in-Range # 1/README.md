# 3870. Count Commas in Range — Iterative

## Problem

Count the commas used when writing every integer from `1` through `n` with standard thousands separators.

## Approach

For the problem's range, each number from `1000` onward contributes one comma. The solution iterates through all values and increments the answer for every value at least `1000`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [3870-Count-Commas-in-Range # 1.py](./3870-Count-Commas-in-Range%20%23%201.py)
