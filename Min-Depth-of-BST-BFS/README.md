# 111. Minimum Depth of Binary Tree — BFS

## Problem

Return the number of nodes on the shortest path from the root of a binary tree to any leaf.

## Approach

Breadth-first search stores each node with its depth in a queue. Because nodes are processed level by level, the depth of the first leaf encountered is the minimum depth.

## Complexity

- Time: `O(n)`
- Space: `O(w), where `w` is the maximum tree width`

## Solution

- [Min-Depth-of-BST-BFS.py](./Min-Depth-of-BST-BFS.py)
