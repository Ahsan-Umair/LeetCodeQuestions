# 67. Add Binary

## Problem

Add two binary strings and return their sum as another binary string.

## Approach

Two indices scan the inputs from right to left. At each position, the two digits and carry are added; modulo two produces the output digit and integer division produces the next carry. Digits are inserted at the front of the result list.

## Complexity

- Time: `O(L²) in this implementation because front insertion into a list shifts existing elements`
- Space: `O(L), where `L` is the length of the result`

## Solution

- [Add-Binary.py](./Add-Binary.py)
