# 387. First Unique Character in a String

Given a string `s`, return the index of its first non-repeating character. If no character appears exactly once, return `-1`.

## Solution

The implementation in `387-First-Unique-Character-in-a-String.py` uses two passes:

1. Count how many times each character appears in `s`.
2. Scan `s` from left to right and return the first index whose character has a frequency of `1`.
3. Return `-1` if every character appears more than once.

The second pass preserves the original order, so the first matching character is the first unique character.

## Examples

```text
Input:  s = "leetcode"
Output: 0
Explanation: 'l' appears once and is the first unique character.
```

```text
Input:  s = "loveleetcode"
Output: 2
Explanation: 'v' is the first character that appears only once.
```

```text
Input:  s = "aabb"
Output: -1
Explanation: Every character appears more than once.
```

## Complexity

- Time: `O(n)`, where `n` is the length of `s`.
- Space: `O(k)`, where `k` is the number of distinct characters in `s`.
