class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        n = len(nums)
        result = []

        for num in nums:
            seen.add(num)



        for i in range(1,n+1):
            if i not in seen:
                result.append(i)

        return result