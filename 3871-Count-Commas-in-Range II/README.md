# 3871. Count Commas in Range II

## Problem

Count all commas used when writing every integer from `1` through `n`, including numbers large enough to contain multiple thousands separators.

## Approach

Each threshold `1000`, `1,000,000`, and so on represents one additional comma contributed by every number at or above that threshold. The solution adds the count of qualifying numbers at each threshold and multiplies the threshold by `1000` for the next group.

## Complexity

- Time: `O(log₁₀₀₀ n)`
- Space: `O(1)`

## Solution

- [3871-Count-Commas-in-Range II.py](./3871-Count-Commas-in-Range%20II.py)
