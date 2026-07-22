class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        # build adj list: parent -> child
        for u, v in edges:
            graph[u].append(v)

        res = [[] for _ in range(n)]
        def dfs(curr, start_ancestor):
            for neighbor in graph[curr]:
                # if the neighbor's list is empty OR the last added ancestor
                #  isn't our starting ancestor
                # - prevents duplicates & acts as visiting set
                if not res[neighbor] or res[neighbor][-1] != start_ancestor:
                    res[neighbor].append(start_ancestor)
                    dfs(neighbor, start_ancestor)
        
        for i in range(n):
            dfs(i, i)

        return res