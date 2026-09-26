# 145. Binary Tree Postorder Traversal

## Problem

Return the postorder traversal of a binary tree.

## Approach

A recursive depth-first search visits the left subtree, then the right subtree, and finally appends the current node.

## Complexity

- Time: `O(n)`
- Space: `O(h) auxiliary recursion space and O(n) for the result`

## Solution

- [BST-PostOrder-Traversal.py](./BST-PostOrder-Traversal.py)
