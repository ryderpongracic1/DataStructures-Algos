import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        counter = 0 # projects chosen
        max_heap = [] # -profit of startable projects
        projects = sorted(list(zip(capital, profits)))
        i = 0
        while i < len(projects):
            c, p = projects[i]
            if w < c:
                break
            heapq.heappush(max_heap, -p)
            i += 1

        while max_heap and counter < k:
            p = -heapq.heappop(max_heap)
            w += p
            counter += 1
            while i < len(projects):
                c, p = projects[i]
                if w < c:
                    break
                heapq.heappush(max_heap, -p)
                i += 1
        return w