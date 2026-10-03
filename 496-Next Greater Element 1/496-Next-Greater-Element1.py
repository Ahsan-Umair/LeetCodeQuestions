class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        n2 = len(nums2)

        for value in nums1:
            j = nums2.index(value)
            found = False

            for k in range(j+1, n2):
                if nums2[k] > value:
                    result.append(nums2[k])
                    found = True
                    break
            
            if found == False:
                result.append(-1)
        return result