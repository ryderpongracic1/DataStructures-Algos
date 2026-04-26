# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, least, most):
            if not node:
                return True
            
            if not (least < node.val < most):
                return False
            left = valid(node.left, least, node.val)
            right = valid(node.right, node.val, most)
            return left and right
        return valid(root, float('-inf'), float('inf'))