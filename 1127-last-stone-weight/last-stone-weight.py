import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap) # top holds largest stone

        # at least 2 stones to be smashed
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap) # heaviest stone
            y = -heapq.heappop(max_heap) # 2nd heaviest
            if x > y: # else they destroy eachother
                heapq.heappush(max_heap, -(x - y))

        if not max_heap:
            return 0

        return -max_heap[0]