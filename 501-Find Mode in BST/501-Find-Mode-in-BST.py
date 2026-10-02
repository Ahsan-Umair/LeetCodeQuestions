# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        frequency = {}
        result = []

        def traverse(node):
            if not node:
                return 

            if node.val in frequency:
                frequency[node.val] +=1
            else:
                frequency[node.val] = 1
            
            traverse(node.left)
            traverse(node.right)
        traverse(root)

        max_frequency = 0

        for key, value in frequency.items():
            if value > max_frequency:
                max_frequency = value
        
        for key, value in frequency.items():
            if value == max_frequency:
                result.append(key)

        return result