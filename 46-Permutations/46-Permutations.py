class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        path = []
        result = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack()
                path.pop()

        backtrack()
        return result