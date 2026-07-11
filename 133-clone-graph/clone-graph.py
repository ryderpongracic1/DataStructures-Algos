"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {} # old node -> new node

        def dfs(node):
            if not node:
                return None
            if node in created:
                return created[node]

            copy = Node(node.val)
            created[node] = copy

            for n in node.neighbors:
                if n:
                    copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)