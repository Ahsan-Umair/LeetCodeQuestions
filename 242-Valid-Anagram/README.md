# 242. Valid Anagram

## Problem

Determine whether string `t` is an anagram of string `s`.

Two strings are anagrams when they contain the same characters with the same frequencies, even if the characters appear in a different order.

## Approach

The `isAnagram` method:

1. Returns `False` immediately when the strings have different lengths.
2. Counts the occurrences of each character in `s`.
3. Counts the occurrences of each character in `t`.
4. Compares the two frequency dictionaries.

The strings are anagrams exactly when their character-frequency dictionaries are equal.

## Why the counts matter

Comparing the set of characters loses information about repetitions. Both
`"aab"` and `"abb"` contain `a` and `b`, but their counts disagree.

| String | Count of `a` | Count of `b` | Anagram of `"aab"` |
|---|---:|---:|---|
| `"aab"` | 2 | 1 | Yes |
| `"aba"` | 2 | 1 | Yes |
| `"abb"` | 1 | 2 | No |

A frequency dictionary records the number of copies of each character and
ignores their positions, so rearranging the characters leaves the counts equal.

## Complexity

- **Time:** $O(n)$, where $n$ is the length of the strings.
- **Space:** $O(n)$ in the worst case for the character-frequency dictionaries.

## Usage

```python
solution = Solution()

solution.isAnagram("anagram", "nagaram")  # True
solution.isAnagram("rat", "car")         # False
```

The implementation is in [242-Valid-Anagram.py](242-Valid-Anagram.py).