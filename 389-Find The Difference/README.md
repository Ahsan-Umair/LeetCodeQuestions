# 389. Find the Difference

Given two strings `s` and `t`, where `t` is formed by shuffling `s` and adding one character, return the added character.

## Solution

The implementation in `389-Find-the-Difference.py` uses two frequency dictionaries:

1. Count the occurrences of each character in `s`.
2. Count the occurrences of each character in `t`.
3. Scan `t` and return the first character that does not appear in `s` or whose frequency in `t` is greater than its frequency in `s`.

Because `t` contains exactly one additional character, that character is either new to `t` or has one higher count than in `s`.

## Examples

```text
Input:  s = "abcd", t = "abcde"
Output: "e"
```

```text
Input:  s = "", t = "y"
Output: "y"
```

```text
Input:  s = "aabbcc", t = "abccadb"
Output: "d"
```

## Complexity

Let `n` be the length of `s`.

- Time: `O(n)`, since both strings are traversed a constant number of times.
- Space: `O(k)`, where `k` is the number of distinct characters.
