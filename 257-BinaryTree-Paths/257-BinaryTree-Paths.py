# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        current_path = []
        paths = []

        def dfs(node):
            if node == None:
                return
            current_path.append(node.val)

            if node.left == None and node.right == None:
                paths.append("->".join(str(x) for x in current_path))

            dfs(node.left)
            dfs(node.right)

            current_path.pop()
        dfs(root)
        return paths
