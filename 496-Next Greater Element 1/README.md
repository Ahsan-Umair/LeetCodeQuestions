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

## Approach: Monotonic Stack + Hash Map

### Intuition
Instead of searching for the next greater element for each query individually (brute force), we can precompute the next greater element for **every** element in `nums2` using a **monotonic decreasing stack**, then store the results in a **hash map** for O(1) lookup.

### Algorithm
1. Iterate through `nums2` from left to right.
2. Maintain a stack. For each element, pop all stack elements that are **smaller** than the current element — the current element is their "next greater element". Store these mappings in a hash map.
3. Push the current element onto the stack.
4. After the loop, any elements remaining in the stack have no next greater element (map to `-1`).
5. Build the result array by looking up each element of `nums1` in the hash map.

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n + m) — where n = len(nums1), m = len(nums2). Each element is pushed/popped from the stack at most once. |
| **Space Complexity** | O(m) — for the stack and the hash map. |

## Solution File

- [`496-Next-Greater-Element1.py`](./496-Next-Greater-Element1.py)
