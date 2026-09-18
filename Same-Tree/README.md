# 100. Same Tree

## Problem

Determine whether two binary trees have identical structures and node values.

## Approach

The trees are compared recursively in matching positions. Two missing nodes match, one missing node fails, and equal current values require both pairs of child subtrees to match.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [Same-Tree.py](./Same-Tree.py)
