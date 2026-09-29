# 292. Nim Game

## Problem

You are playing a game with a pile of stones. Each turn, a player can remove 1, 2, or 3 stones. The player who removes the last stone wins.

Given `n`, determine whether the current player can win the game.

## Key Observation

The winning condition follows a simple pattern:

- If `n % 4 == 0`, the first player loses.
- Otherwise, the first player wins.

This works because every full cycle of 4 stones is a losing position for the player whose turn it is.

## Example

- `n = 4` -> `False`
- `n = 5` -> `True`
- `n = 6` -> `True`
- `n = 7` -> `True`
- `n = 8` -> `False`

## Approach

The solution checks whether the number of stones is divisible by 4:

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True
```

## Time Complexity

- Time: `O(1)`
- Space: `O(1)`

## Summary

This is a classic mathematical game strategy problem. The pattern is based on the fact that positions that are multiples of 4 are losing states, so the player can force a win whenever `n` is not divisible by 4.
