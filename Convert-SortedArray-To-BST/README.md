# 108. Convert Sorted Array to Binary Search Tree

## Problem

Convert a sorted integer array into a height-balanced binary search tree.

## Approach

The middle value becomes the current root, and the left and right slices are recursively converted into its subtrees. Choosing the midpoint at every level keeps the tree balanced.

## Complexity

- Time: `O(n log n) in this implementation because array slicing copies elements`
- Space: `O(n) peak auxiliary space from slices and recursion`

## Solution

- [Convert-SortedArray-To-BST.py](./Convert-SortedArray-To-BST.py)
