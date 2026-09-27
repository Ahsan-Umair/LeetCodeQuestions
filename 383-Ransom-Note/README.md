# 383. Ransom Note

Given two strings, `ransomNote` and `magazine`, determine whether it is possible to construct `ransomNote` using only the letters available in `magazine`.

Each letter in `magazine` can be used at most once.

## Example

Input:
- `ransomNote = "a"`
- `magazine = "b"`

Output:
- `false`

Because there is no `'a'` in `magazine`.

## Approach

This solution converts `magazine` into a list and then checks each character in `ransomNote`:

- If the character exists in the available letters, it is removed from the list.
- If the character does not exist, the function immediately returns `False`.
- If all characters are matched successfully, it returns `True`.

This works because we are effectively simulating the use of letters from `magazine` while building the ransom note.

## Python Implementation

See [383-Ransom-Note.py](383-Ransom-Note.py).

## Time Complexity

- Let `n` be the length of `ransomNote` and `m` be the length of `magazine`.
- The algorithm checks each character in `ransomNote` and may scan the list of available letters.
- Overall complexity: `O(n * m)` in the worst case.

## Space Complexity

- The code creates a list copy of `magazine`.
- Space complexity: `O(m)`.
