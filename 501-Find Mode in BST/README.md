# 501. Find Mode in Binary Search Tree

## Problem

Given the root of a binary search tree, return all the mode(s)—the value(s)
that appear most frequently in the tree. If multiple values have the highest
frequency, return all of them in any order.

## Solution

The implementation in
[`501-Find-Mode-in-BST.py`](./501-Find-Mode-in-BST.py) performs a depth-first
traversal and stores the frequency of each node value in a dictionary. After
the traversal, it makes two passes over the frequency table:

1. Find the highest frequency.
2. Collect every value whose frequency equals that maximum.

The `TreeNode` definition is supplied by the LeetCode execution environment.

### Why it works

The traversal visits every node exactly once and increments the count for its
value. Consequently, the frequency table contains the exact occurrence count
for every value in the tree. Selecting all values with the largest count
returns precisely the tree's modes.

### Complexity

- **Time:** `O(n)`, where `n` is the number of nodes
- **Space:** `O(n)` for the frequency dictionary, plus `O(h)` recursion stack
  space, where `h` is the tree height

## Usage

```python
# With the platform-provided TreeNode class:
solution = Solution()
result = solution.findMode(root)
```
