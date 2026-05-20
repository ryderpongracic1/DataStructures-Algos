import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = [] # -profit of startable projects
        projects = sorted(list(zip(capital, profits)))

        i = 0
        counter = 0 # projects chosen
        while counter < k:
            while i < len(projects):
                c, p = projects[i]
                if w < c:
                    break
                heapq.heappush(max_heap, -p)
                i += 1
            if not max_heap:
                break
            p = -heapq.heappop(max_heap)
            w += p
            counter += 1
        return w