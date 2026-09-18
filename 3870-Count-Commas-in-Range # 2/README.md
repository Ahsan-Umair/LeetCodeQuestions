# 3870. Count Commas in Range — Formula

## Problem

Count the commas used when writing every integer from `1` through `n` with standard thousands separators.

## Approach

For the problem's range, the integers `1000...n` each contribute one comma. The boolean expression handles values below `1000`, while `n - 999` directly counts qualifying values otherwise.

## Complexity

- Time: `O(1)`
- Space: `O(1)`

## Solution

- [3870-Count-Commas-in-Range # 2.py](./3870-Count-Commas-in-Range%20%23%202.py)
