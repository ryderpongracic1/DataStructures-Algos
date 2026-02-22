# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, depth):
            if not node: # Null
                return float('inf')
            if not node.left and not node.right: # Leaf
                return depth + 1

            left = dfs(node.left, depth) + 1
            right = dfs(node.right, depth) + 1

            return min(left, right)
        return dfs(root, 0)