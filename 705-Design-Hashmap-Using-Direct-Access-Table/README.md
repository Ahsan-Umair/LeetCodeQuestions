# 705. Design HashSet — Direct-Access Table

## Problem

Implement a set of integer keys with `add`, `remove`, and `contains` operations without using a built-in hash-set type.

## Approach

A boolean array indexed directly by key stores membership. Adding or removing a key changes its slot, and checking a key returns the boolean at that index.

## Complexity

- Time: `O(1) per operation`
- Space: `O(U), where `U = 1,000,001` is the supported key range`

## Solution

- [705-Design-Hashmap-Using-Direct-Access-Table.py](./705-Design-Hashmap-Using-Direct-Access-Table.py)
