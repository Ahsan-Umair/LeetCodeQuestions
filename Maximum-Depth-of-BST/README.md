# 104. Maximum Depth of Binary Tree

## Problem

Return the maximum number of nodes along a path from the root of a binary tree to a leaf.

## Approach

The solution recursively computes the maximum depth of the left and right subtrees and adds one for the current node. An empty subtree contributes zero.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [Maximum-Depth-of-BST.py](./Maximum-Depth-of-BST.py)
