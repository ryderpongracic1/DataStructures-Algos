import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        min_costs = {i: float('inf') for i in range(n)}
        min_costs[0] = 0
        heap = [(0, 0)]

        # Djikstra's BFS
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > min_costs[node]:
                continue
            min_costs[node] = cost

            if node == n - 1:
                return cost
            for v, w in adj[node]:
                curr_cost = cost + w
                if curr_cost < min_costs[v]:
                    min_costs[v] = curr_cost
                    heapq.heappush(heap, (curr_cost, v))
        return -1