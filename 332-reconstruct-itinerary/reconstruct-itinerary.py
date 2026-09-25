from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for dept, arrv in tickets:
            heapq.heappush(graph[dept], arrv)

        route = []
        def dfs(airport):
            while graph[airport]:
                arrv = heapq.heappop(graph[airport])
                dfs(arrv)
            route.append(airport) # fully explored
        
        dfs('JFK')
        return route[::-1]