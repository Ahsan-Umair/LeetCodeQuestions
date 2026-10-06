# 771. Jewels and Stones

## Problem

Given two strings:

- `jewels` contains the types of stones that are jewels.
- `stones` contains the stones you have.

Return the number of stones that are also jewels. Letter case matters, so uppercase
and lowercase letters are treated as different types.

## Solution

`Solution.numJewelsInStones` iterates through every character in `stones` and
checks whether it occurs in `jewels`. The counter is incremented for each match.

## Complexity

- **Time:** `O(len(stones) * len(jewels))` in the worst case because membership is
  checked in a string.
- **Space:** `O(1)` auxiliary space.

## Usage

```python
solution = Solution()
result = solution.numJewelsInStones("aA", "aAAbbbb")
print(result)  # 3
```

