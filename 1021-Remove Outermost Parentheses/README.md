# 1021. Remove Outermost Parentheses

## Problem

Given a valid parentheses string, remove the outermost pair of parentheses from every primitive valid parentheses substring and return the resulting string.

A primitive parentheses string is a non-empty valid parentheses string that cannot be split into two non-empty valid parentheses strings.

For example, `(()())()` is made of the primitive strings `(()())` and `()`. Removing each primitive's outermost pair produces `()()`.

## Approach

The `Solution.removeOuterParentheses` method tracks the current nesting depth with `count`:

1. When an opening parenthesis is found, it is included only if the current depth is greater than zero.
2. The depth is then increased.
3. When a closing parenthesis is found, the depth is decreased first.
4. The closing parenthesis is included only if the resulting depth is greater than zero.

This excludes exactly the opening parenthesis that starts a primitive component and the closing parenthesis that ends it, while preserving all inner parentheses.

## Complexity

Let `n` be the length of `s`.

- **Time:** `O(n^2)` in the worst case for this implementation because repeated string concatenation can copy the current result. With a list builder and `"".join(...)`, the approach can be implemented in `O(n)` time.
- **Space:** `O(n)` for the returned string and the accumulated result.

## Usage

```python
solution = Solution()
answer = solution.removeOuterParentheses("(()())()")
# answer == "()()"
```

The implementation is contained in [`1021. Remove Outermost Parentheses.py`](./1021.%20Remove%20Outermost%20Parentheses.py).
