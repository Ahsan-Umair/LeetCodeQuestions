# 682. Baseball Game

## Problem

Evaluate a sequence of baseball scoring operations and return the total score after all operations.

## Approach

A list acts as a stack of valid round scores. Integers add a new score, `D` doubles the previous score, `+` sums the previous two scores, and `C` removes the most recent score.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

- [682-BaseBall-Game.py](./682-BaseBall-Game.py)
