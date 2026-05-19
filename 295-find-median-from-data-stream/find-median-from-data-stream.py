import heapq
class MedianFinder:

    def __init__(self):
        self.small_max_heap = [] # smaller half max-heap of -vals
        self.large_min_heap = [] # largest half min-heap of vals

    def addNum(self, num: int) -> None:
        largest_small_val = -heapq.heappushpop(self.small_max_heap, -num)
        heapq.heappush(self.large_min_heap, largest_small_val)
    
        # small half can be at most 1 larger than large half
        if len(self.large_min_heap) > len(self.small_max_heap):
            smallest_large_val = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -smallest_large_val)

    def findMedian(self) -> float:
        if (len(self.small_max_heap) + len(self.large_min_heap)) % 2 == 0:
            return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2

        # odd stream -> median in small_max_heap
        return -self.small_max_heap[0]