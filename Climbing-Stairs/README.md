# 70. Climbing Stairs

## Problem

Count the distinct ways to reach the top of a staircase when each move climbs one or two steps.

## Approach

The number of ways to reach a step is the sum of the previous two counts. The solution iteratively maintains only those two values instead of storing the full dynamic-programming table.

## Why the previous two counts are added

The final move to step `i` must come from either step `i - 1` with a one-step
move or step `i - 2` with a two-step move. These choices have different final
moves, so their counts can be added without counting a path twice.

Before each iteration, `ways_prev1` stores the count for `i - 2`, and
`ways_prev2` stores the count for `i - 1`.

For `n = 4`:

| Step `i` | `ways_prev1` before addition | `ways_prev2` before addition | New count `ways` |
|---|---|---|---|
| `2` | `1` | `1` | `2` |
| `3` | `1` | `2` | `3` |
| `4` | `2` | `3` | `5` |

After each addition, the old `ways_prev2` becomes `ways_prev1`, and the new
count becomes `ways_prev2`. The method returns `5` for four steps. The initial
count of `1` for zero steps represents taking no moves; one step also has
exactly one way, handled by the early return.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Climbing-Stairs.py](./Climbing-Stairs.py)
