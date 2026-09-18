# 705. Design HashSet — List

## Problem

Implement a set of integer keys with `add`, `remove`, and `contains` operations without using a built-in hash-set type.

## Approach

Keys are stored in a Python list. `add` first checks for duplicates, `remove` deletes an existing key, and `contains` performs a membership search.

## Complexity

- Time: `O(n) per operation in the worst case`
- Space: `O(n)`

## Solution

- [705-Design-Hashmap-Using-List.py](./705-Design-Hashmap-Using-List.py)
