# 101. Symmetric Tree

## Problem

Determine whether a binary tree is a mirror of itself around its center.

## Approach

A recursive helper compares two subtrees in mirrored order: left with right and right with left. Corresponding values must match, and missing nodes must occur in pairs.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [SymmetricTree.py](./SymmetricTree.py)
