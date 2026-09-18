# 590. N-ary Tree Postorder Traversal

## Problem

Return the postorder traversal of an N-ary tree.

## Approach

A recursive depth-first search visits every child from left to right before appending the current node's value.

## Complexity

- Time: `O(n)`
- Space: `O(h) auxiliary recursion space and O(n) for the result`

## Solution

- [590-N-Ary-Tree-PostOrder-Traversal.py](./590-N-Ary-Tree-PostOrder-Traversal.py)
