'''
NOTES
- All positive weights: Djikstra's finds abs shortest path
- shortest path will never revisit node - 'at most once' switch is satisfied

APPROACH: Dijkastra's on modified graph
i) Build adj list
- for every [u, v, w]:
 - add (v, w) to adj[u]
 - add (u, 2w) to adj[v]
ii) Init Dijkstra's State:
- create min_costs init to inf for all nodes
- create min heap to store (current cost, current node) init with (0, 0)
iii) Process Heap
- pop min
- check if current cost > min_costs[node]: already found better path
- check if reached target (n - 1)
- Explore neighbors (adj[node])
 - new_cost = current cost + w
 - if new_cost < min_costs[v]: update & push to heap
'''
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