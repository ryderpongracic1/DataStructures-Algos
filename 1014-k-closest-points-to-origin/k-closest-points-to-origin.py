import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [] # -dist, [x, y]
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(max_heap, (dist, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = [0] * k
        for i, (_, coords) in enumerate(max_heap):
            res[i] = coords
        return res
