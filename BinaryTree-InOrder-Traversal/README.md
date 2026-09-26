# 94. Binary Tree Inorder Traversal

## Problem

Return the inorder traversal of a binary tree.

## Approach

A recursive depth-first search visits the left subtree, appends the current node, and then visits the right subtree.

## Complexity

- Time: `O(n)`
- Space: `O(h) auxiliary recursion space and O(n) for the result`

## Solution

- [BinaryTree-InOrder-Traversal.py](./BinaryTree-InOrder-Traversal.py)
