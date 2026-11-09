# 234. Palindrome Linked List

## Problem

Determine whether a singly linked list reads the same from left to right and
right to left.

## Approach

The solution uses the fast and slow pointer technique to locate the midpoint
of the list. It then reverses the second half in place and compares that
reversed half with the list's first half. Any different pair of values means
the list is not a palindrome; if every value matches, it is a palindrome.

The linked list is modified while the second half is reversed and is not
restored afterward.

## Worked example

For `head = [1, 2, 3, 2, 1]`:

1. `slow` and `fast` both start at the first `1`.
2. After one loop iteration, `slow` is at `2` and `fast` is at `3`.
3. After the next iteration, `slow` is at `3` and `fast` is at the final `1`.
   Since `fast.next` is `None`, the midpoint search stops.
4. Reversing the part starting at `slow` changes `[3, 2, 1]` into `[1, 2, 3]`.
5. `left` starts at the original head and `right` starts at the reversed head.
   The comparisons are `1 == 1`, `2 == 2`, and `3 == 3`.
6. `right` becomes `None`, so the method returns `True`.

For an odd-length list, this implementation includes the middle value in
the reversed part. It matches itself in the final comparison. For an
even-length list, the reversed part contains exactly half the nodes.

## Edge cases

- `[1]` returns `True`.
- `[1, 1]` returns `True`.
- `[1, 2]` returns `False` at the first comparison.
- `[1, 2, 2, 1]` returns `True` after comparing the two pairs.

## Keeping track of nodes during reversal

`prev` points to the head of the part already reversed, while `current`
points to the next node to reverse. Each iteration performs four steps:

1. Save `current.next` in `temp` before changing the link.
2. Set `current.next = prev` to point the current node backward.
3. Move `prev` to `current`, making it the new reversed head.
4. Move `current` to `temp` to continue through the original list.

Saving `temp` preserves the route to the remaining nodes. After the loop,
`current` is `None`, and `prev` is the head used by the comparison loop.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [234-Palindrome-LinkedList.py](./234-Palindrome-LinkedList.py)
