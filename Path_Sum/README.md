# 112. Path Sum

## Problem

Determine whether a binary tree contains a root-to-leaf path whose values add up to the target.

## Approach

At each node, its value is subtracted from the remaining target. A leaf succeeds when its value equals the remaining target; otherwise, the search recursively checks either child.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [Path_Sum.py](./Path_Sum.py)
