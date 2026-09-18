# 804. Unique Morse Code Words

## Problem

Translate each lowercase word into Morse code and return the number of distinct transformations.

## Approach

A 26-entry table maps letters to Morse strings. Each word is translated by indexing that table with its characters, and the completed transformations are placed in a set.

## Complexity

- Time: `O(c), where `c` is the total number of input characters`
- Space: `O(c) for the unique encoded strings`

## Solution

- [804-Unique-Morse-Code-Words.py](./804-Unique-Morse-Code-Words.py)
