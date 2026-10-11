# 657. Robot Return to Origin

## Problem

Given a string of moves made by a robot on a 2D plane, determine whether the robot returns to its starting position after completing all moves.

Each character represents one step:

- `U`: move up
- `D`: move down
- `L`: move left
- `R`: move right

## Approach

The robot ends at the origin when opposite movements cancel each other out:

- The number of `U` moves must equal the number of `D` moves.
- The number of `L` moves must equal the number of `R` moves.

The solution checks both conditions using `str.count()`.

## Complexity

- **Time:** `O(n)`, where `n` is the length of `moves`. The string is scanned a constant number of times.
- **Space:** `O(1)`, excluding the input string.

## Implementation

See [657-Robot Return to Origin.py](657-Robot%20Return%20to%20Origin.py).

```python
class Solution:

    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count(
            "L"
        ) == moves.count("R")
```

## Examples

- `"UD"` returns `True` because the up and down moves cancel.
- `"UUL"` returns `False` because the robot does not return to the origin.
