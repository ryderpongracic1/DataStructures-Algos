# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        ans = 0
        queue.append((root, float('-inf')))

        while queue:
            node, most = queue.popleft()
            if node.val >= most:
                ans += 1
                most = node.val
            if node.left:
                queue.append((node.left, most))
            if node.right:
                queue.append((node.right, most))
        return ans