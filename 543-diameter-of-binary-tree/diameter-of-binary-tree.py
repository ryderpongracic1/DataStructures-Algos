# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Longest path through a node is left subtree height + right subtree height
# Find longest path through every node & keep global max
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            diameter = left + right
            self.diameter = max(self.diameter, diameter)
            return 1 + max(left, right)
            
        height(root)
        return self.diameter