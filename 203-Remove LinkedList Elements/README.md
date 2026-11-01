# 203. Remove Linked List Elements

## Problem

Given the head of a singly linked list and an integer `val`, remove every node whose value equals `val` and return the updated head.

## Approach

The solution updates the list in place:

1. Remove matching nodes from the beginning of the list by advancing `head`.
2. Traverse the remaining list with `current`.
3. When `current.next` contains `val`, bypass that node by setting `current.next` to `current.next.next`.
4. Otherwise, advance `current` to the next node.

The pointer stays in place after removing a node so consecutive matching nodes are handled correctly.

## Example

```text
Input:  head = [1, 2, 6, 3, 4, 5, 6], val = 6
Output: [1, 2, 3, 4, 5]
```

## Consecutive removals

For `head = [6, 6, 1, 6, 6, 2]` and `val = 6`:

1. The first loop advances `head` past both leading `6` nodes to `1`.
2. With `current` at `1`, the next node is `6`, so that node is bypassed.
3. `current` stays at `1`. Its new next node is also `6`, so it is bypassed too.
4. The next node is now `2`, so `current` advances to it and the scan finishes.

The returned list is `[1, 2]`. Moving `current` immediately after a removal
would skip checking its new next node.

## Edge cases

| Input list | `val` | Returned list |
|---|---|---|
| `[]` | `6` | `[]` |
| `[6, 6]` | `6` | `[]` |
| `[1, 2]` | `6` | `[1, 2]` |
| `[1, 6, 6]` | `6` | `[1]` |

## Complexity

- **Time:** `O(n)`, where `n` is the number of nodes in the list.
- **Space:** `O(1)`, because nodes are removed by changing pointers in place.

## Python Implementation

See [203-Remove-LinkedList-Elements.py](./203-Remove-LinkedList-Elements.py).

## Reference

- [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
