# 226. Invert Binary Tree

## Problem

Invert a binary tree by swapping the left and right children of every node.

## Approach

Use recursion to process the tree in place. For each node, swap its left and right children, then recursively invert the two swapped subtrees. An empty tree is returned unchanged.

## Complexity

- Time: `O(n)`, where `n` is the number of nodes
- Space: `O(h) recursion depth`, where `h` is the tree height

## Solution

- [226-Invert-BinaryTree.py](./226-Invert-BinaryTree.py)
