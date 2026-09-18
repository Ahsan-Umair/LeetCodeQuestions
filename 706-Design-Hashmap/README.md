# 706. Design HashMap

## Problem

Implement an integer-to-integer map with `put`, `get`, and `remove` operations without using a built-in hash-table type.

## Approach

A direct-access array uses each key as an index. The sentinel value `-1` represents a missing key; storing, retrieving, and removing values therefore require one indexed access.

## Complexity

- Time: `O(1) per operation`
- Space: `O(U), where `U = 1,000,001` is the supported key range`

## Solution

- [706-Design-Hashmap.py](./706-Design-Hashmap.py)
