'''
# NOTES
- Split grid until each grid is 1x1: always leaf node
- Return up call stack: look at each 4 children
- 4 children: all leaf + all same val = parent is leaf

'''
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, length):
            if length == 1:
                return Node(grid[r][c], True, None, None, None, None)

            half = length // 2
            tL = dfs(r, c, half)
            tR = dfs(r, c + half, half)
            bL = dfs(r + half, c, half)
            bR = dfs(r + half, c + half, half)

            # parent is leaf node
            if tL.isLeaf and tR.isLeaf and bL.isLeaf and bR.isLeaf and tL.val == tR.val == bL.val == bR.val:
                return Node(tL.val, True, None, None, None, None)
            return Node(0, False, tL, tR, bL, bR)
        return dfs(0, 0, len(grid))