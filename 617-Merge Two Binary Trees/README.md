# 617. Merge Two Binary Trees

## Problem

Given the roots of two binary trees, merge them into a single binary tree:

- If both nodes exist at the same position, add their values.
- If only one node exists, keep that node and its subtree.
- If neither node exists, the merged position is empty.

The solution is implemented in [`617-Merge Two Binary Trees.py`](./617-Merge%20Two%20Binary%20Trees.py).

## Approach

The `mergeTrees` method uses depth-first recursion:

1. Return `None` when both nodes are missing.
2. Return the existing node when only one node is missing.
3. Add the two node values when both nodes exist.
4. Recursively merge the left and right children.

The first tree is modified in place. Its nodes are reused for the merged result whenever both input nodes exist.

## Example

For these trees:

```text
Tree 1:        1           Tree 2:        2
              / \                       / \
             3   2                     1   3
            /                             \
           5                               4
```

The merged tree is:

```text
              3
             / \
            4   5
           / \   \
          5   4   4
```

## Complexity

- **Time:** `O(n)`, where `n` is the number of positions visited across the two trees.
- **Auxiliary space:** `O(h)`, where `h` is the height of the deeper tree, due to the recursive call stack.

## LeetCode Signature

```python
def mergeTrees(
    self,
    root1: TreeNode | None,
    root2: TreeNode | None,
) -> TreeNode | None:
```
