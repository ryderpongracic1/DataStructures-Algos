import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        projects = sorted(zip(capital, profits))

        i = 0 # projects idx
        for _ in range(k):
            # more projects & can afford them
            while i < len(projects) and w >= projects[i][0]:
                # add profit to avaiable projects
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # can't afford any projects
            if not max_heap:
                break

            # add profit of best project
            w += -heapq.heappop(max_heap)
        return w