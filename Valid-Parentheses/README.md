# 20. Valid Parentheses

## Problem

Determine whether every bracket in a string is closed by the correct bracket in the correct order.

## Approach

Opening brackets are pushed onto a stack. For a closing bracket, the solution verifies that the stack is nonempty and that its top matches the required opening bracket. The string is valid only if the stack is empty at the end.

## Stack walkthrough

For `s = "([{}])"`, the stack tracks opening brackets still waiting to close:

| Character | Action | Stack afterward |
|---|---|---|
| `(` | Push the opening bracket | `['(']` |
| `[` | Push the opening bracket | `['(', '[']` |
| `{` | Push the opening bracket | `['(', '[', '{']` |
| `}` | Pop and match `{` | `['(', '[']` |
| `]` | Pop and match `[` | `['(']` |
| `)` | Pop and match `(` | `[]` |

The stack is empty at the end, so the method returns `True`.

## Three ways validation can fail

- `")"` returns `False` because there is no opening bracket to match.
- `"([)]"` returns `False` because `)` encounters `[` at the top of the stack.
  The most recent opening bracket must close first.
- `"(("` returns `False` because opening brackets remain after the scan.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

- [Valid-Parentheses.py](./Valid-Parentheses.py)
