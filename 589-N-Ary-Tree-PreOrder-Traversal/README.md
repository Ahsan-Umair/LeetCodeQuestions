# 589. N-ary Tree Preorder Traversal

## Problem

Return the preorder traversal of an N-ary tree.

## Approach

A recursive depth-first search appends the current node before recursively visiting its children from left to right.

## Complexity

- Time: `O(n)`
- Space: `O(h) auxiliary recursion space and O(n) for the result`

## Solution

- [589-N-Ary-Tree-PreOrder-Traversal.py](./589-N-Ary-Tree-PreOrder-Traversal.py)
