# 110. Balanced Binary Tree

## Problem

Determine whether every node in a binary tree has left and right subtree heights that differ by at most one.

## Approach

A postorder depth-first search returns each subtree's height. The sentinel `-1` is propagated as soon as an unbalanced subtree is found, so height and balance are computed in the same traversal.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [Balanced-BST.py](./Balanced-BST.py)
