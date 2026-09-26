# 559. Maximum Depth of N-ary Tree

## Problem

Return the maximum number of nodes along a path from the root of an N-ary tree to a leaf.

## Approach

A recursive depth-first search computes the maximum depth among all children of a node and adds one for the current node. An empty tree returns zero.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth`

## Solution

- [559-Max-Depth=of=NArray-Tree.py](./559-Max-Depth%3Dof%3DNArray-Tree.py)
