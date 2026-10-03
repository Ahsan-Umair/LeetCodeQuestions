# 496. Next Greater Element I

## Problem Link
[LeetCode 496 - Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

## Difficulty
**Easy**

## Problem Description

The **next greater element** of some element `x` in an array is the **first greater element** that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

## Examples

### Example 1
```
Input:  nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Explanation:
  - For 4: No element to its right in nums2 is greater → -1
  - For 1: The first greater element to its right in nums2 is 3 → 3
  - For 2: No element to its right in nums2 is greater → -1
```

### Example 2
```
Input:  nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]

Explanation:
  - For 2: The first greater element to its right in nums2 is 3 → 3
  - For 4: No element to its right in nums2 is greater → -1
```

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10⁴`
- All integers in `nums1` and `nums2` are **unique**.
- All integers of `nums1` also appear in `nums2`.

## Approach: Brute Force (Linear Scan)

### Intuition
For each element in `nums1`, find its position in `nums2` using `list.index()`, then scan rightward from that position to find the first element that is strictly greater.

### Algorithm
1. For each `value` in `nums1`:
   - Find its index `j` in `nums2` using `nums2.index(value)`.
   - Iterate from `j + 1` to the end of `nums2`.
   - If an element greater than `value` is found, append it to the result and break.
   - If no greater element is found, append `-1`.
2. Return the result array.

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n × m) — where n = len(nums1), m = len(nums2). For each element in nums1, we search for its index and then scan rightward. |
| **Space Complexity** | O(n) — for the result array. |

## Solution File

- [`496-Next-Greater-Element1.py`](./496-Next-Greater-Element1.py)
