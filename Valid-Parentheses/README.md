# 20. Valid Parentheses

## Problem

Determine whether every bracket in a string is closed by the correct bracket in the correct order.

## Approach

Opening brackets are pushed onto a stack. For a closing bracket, the solution verifies that the stack is nonempty and that its top matches the required opening bracket. The string is valid only if the stack is empty at the end.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

- [Valid-Parentheses.py](./Valid-Parentheses.py)
