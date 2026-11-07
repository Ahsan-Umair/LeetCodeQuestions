# 12. Integer to Roman

## Problem

Convert an integer into its Roman numeral representation.

## Approach

The solution processes Roman numeral values from largest to smallest, including
the subtractive pairs `CM`, `CD`, `XC`, `XL`, `IX`, and `IV`. While the
remaining number is at least the current value, its symbol is appended and the
value is subtracted. Processing denominations in descending order produces the
canonical Roman numeral.

## Worked example

For `num = 1994`, the matching values are taken in this order:

| Value taken | Symbol appended | Remaining number | Result so far |
|---|---|---|---|
| `1000` | `M` | `994` | `M` |
| `900` | `CM` | `94` | `MCM` |
| `90` | `XC` | `4` | `MCMXC` |
| `4` | `IV` | `0` | `MCMXCIV` |

Values larger than the remaining number are skipped. Subtractive pairs must
appear before their smaller values; for example, `4` is written as `IV`
instead of four `I` symbols.

## Boundary cases

The problem accepts integers from `1` through `3999`.

- `1` returns `I`.
- `4` returns `IV`, and `9` returns `IX`.
- `3999` returns `MMMCMXCIX`.

## Why the mapping order matters

The loop visits the entries in the order written in `roman`. Keeping larger
values before smaller ones lets the method finish each denomination before
moving on. The `while` loop also allows a symbol to be appended more than once.

For `58`, the method takes `50` (`L`), then `5` (`V`), then three `1` values
(`III`), returning `LVIII`. A smaller value placed too early could consume the
remaining number before its larger symbol is considered, so the mapping must
stay in descending value order.

## Complexity

- Time: `O(n)` where `n` is the number of symbols in the result
- Space: `O(n)` for the result

## Solution

- [12-Integer-To-Roman.py](./12-Integer-To-Roman.py)
