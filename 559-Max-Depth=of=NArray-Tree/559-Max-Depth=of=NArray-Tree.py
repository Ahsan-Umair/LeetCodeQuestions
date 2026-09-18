"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
        

        def dfs(node):
            depth = 0

            for child in node.children:
                max_depth = dfs(child)

                depth = max(depth, max_depth) 
            return depth + 1
        return dfs(root)
            

