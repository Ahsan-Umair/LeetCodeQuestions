# 111. Minimum Depth of Binary Tree — DFS

## Problem

Return the number of nodes on the shortest path from the root of a binary tree to any leaf.

## Approach

Recursive depth-first search handles single-child nodes separately so a missing child is not incorrectly treated as a zero-length leaf path. When both children exist, it takes the smaller recursive depth and adds one.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [Min-Depth-of-BST-DFS.py](./Min-Depth-of-BST-DFS.py)
