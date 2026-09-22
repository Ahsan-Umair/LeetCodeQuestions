# 257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order. Each path is represented with `->` between node values.

## Approach

The solution performs a depth-first search with backtracking:

1. Add the current node's value to `current_path`.
2. If the node is a leaf, convert the path to a string and add it to `paths`.
3. Recursively visit the left and right children.
4. Remove the current node's value before returning to the parent.

If `root` is `None`, the traversal does not visit any nodes and returns an empty list.

## Correctness

DFS visits every node reachable from the root. Whenever it reaches a leaf, `current_path` contains exactly the values from the root to that leaf, so the generated string is one valid root-to-leaf path. Backtracking removes each node after its subtree is processed, ensuring that every subsequent path starts with the correct root-to-leaf sequence. Therefore, `paths` contains all and only the binary tree's root-to-leaf paths.

## Complexity

Let $n$ be the number of nodes, $h$ the tree height, and $k$ the total length of all output path strings.

- **Time:** $O(nh + k)$, including traversal, path construction, and output generation.
- **Auxiliary space:** $O(h)$ for the recursion stack and the shared path.
- **Output space:** $O(k)$ for the returned path strings.

## Example

For this tree:

```text
    1
   / \
  2   3
   \
    5
```

The result is:

```python
["1->2->5", "1->3"]
```
