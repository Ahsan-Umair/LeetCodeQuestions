# 228. Summary Ranges

## Problem

Given a sorted array of unique integers, summarize each consecutive range as
either a single value or a range from its first value to its last value.

## Approach

The solution tracks the start index of the current consecutive range. As the
array is scanned, a break is found whenever the next value is not one greater
than the previous value. The completed range is then formatted and the start
index is moved to the new range. The final range is appended after the scan.

## Worked example

For `nums = [0, 1, 2, 4, 5, 7]`, `start` begins at index `0`.

| Current value | What happens | `ans` after this step |
|---|---|---|
| `1` | Continues the range starting at `0` | `[]` |
| `2` | Continues that range | `[]` |
| `4` | Closes `0->2`; moves `start` to index `3` | `["0->2"]` |
| `5` | Continues the range starting at `4` | `["0->2"]` |
| `7` | Closes `4->5`; moves `start` to index `5` | `["0->2", "4->5"]` |
| End of scan | Appends the final single value | `["0->2", "4->5", "7"]` |

The final append happens after the loop because the last range has no next
value to reveal that it is complete.

## Edge cases

- `[]` returns `[]`.
- `[5]` returns `["5"]`, without an arrow for a single value.
- `[-2, -1, 0]` returns `["-2->0"]`; consecutive ranges can cross zero.

## Input assumptions and output order

The input is already sorted in strictly increasing order, so it contains no
duplicate values. Before each loop check, the values from `start` through
`i - 1` form one consecutive range. A gap closes that range, and the new value
starts the next one.

The method reads `nums` without modifying it. Ranges are returned in input
order, and each input value belongs to exactly one returned range. For
example, `[1, 3, 5]` returns `["1", "3", "5"]`: isolated values stay separate
rather than being joined across gaps.

## Complexity

- Time: `O(n)`
- Space: `O(n)` for the result

## Solution

- [228-Summary-ranges.py](./228-Summary-ranges.py)
