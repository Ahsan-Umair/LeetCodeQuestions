# 2265. Count Nodes Equal to Average of Subtree

## Problem

Count the nodes in a binary tree whose value equals the integer average of all values in that node's subtree.

## Approach

A postorder depth-first search returns the sum and node count for each subtree. After combining the left subtree, right subtree, and current node, the solution computes the integer average and increments a shared counter when it matches the node value.

## Complexity

- Time: `O(n)`
- Space: `O(h) recursion depth, where `h` is the tree height`

## Solution

- [2265-Count-Nodes-Equal-To-SubTree.py](./2265-Count-Nodes-Equal-To-SubTree.py)
