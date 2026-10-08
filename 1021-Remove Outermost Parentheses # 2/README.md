# 1021. Remove Outermost Parentheses

## Problem

Given a valid parentheses string, remove the outermost pair of parentheses
from every primitive valid parentheses substring and return the resulting
string.

A primitive valid parentheses string is a non-empty valid parentheses string
that cannot be split into two non-empty valid parentheses strings. For
example, `(()())()` contains the primitive strings `(()())` and `()`, so the
result is `()()`.

## Approach

The `Solution.removeOuterParentheses` method scans the string while tracking
the current nesting depth with `count`.

1. Increment `count` for `(` and decrement it for `)`.
2. When `count` becomes zero, a complete primitive substring has been found.
3. Append the substring between `start + 1` and `i`, which removes that
   primitive's outermost pair.
4. Move `start` to the beginning of the next primitive substring.

Because a primitive substring returns the depth to zero only at its final
character, the extracted slice excludes exactly its first and last
parentheses.

## Complexity

Let `n` be the length of `s`.

- **Time:** `O(n^2)` in the worst case because repeated string concatenation
  can copy the accumulated result.
- **Space:** `O(n)` for the returned string and intermediate result.

## Usage

```python
solution = Solution()
answer = solution.removeOuterParentheses("(()())()")
# answer == "()()"
```

The implementation is in
[`1021-Remove Outermost Parentheses #2.py`](./1021-Remove%20Outermost%20Parentheses%20%232.py).
