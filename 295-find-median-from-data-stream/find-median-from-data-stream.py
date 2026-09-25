"""
**Double Heap Approach**
- heap1 maxheap of smallest values: top gives largest from small half
- heap2 minheap of largest values: top gives smallest from large half
- heap1 Top & heap2 Top will contain the median

Heap Rules:
- len(heap1) <= len(heap2) <= len(heap1) + 1
- heap1[0] <= heap2[0]

Adding:
- Push to heap1 and then pop from heap1 to bubble new largest of small half
- Push to heap2
- Rebalance if needed
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.heap1 = [] # MaxHeap (negative values)
        self.heap2 = [] # MinHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1, -num)
        v = -heapq.heappop(self.heap1)
        heapq.heappush(self.heap2, v)

        if len(self.heap1) > len(self.heap2):
            v = -heapq.heappop(self.heap1)
            heapq.heappush(self.heap2, v)
        elif len(self.heap2) > len(self.heap1) + 1:
            v = heapq.heappop(self.heap2)
            heapq.heappush(self.heap1, -v)

    def findMedian(self) -> float:
        # print(self.heap1, self.heap2)
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0] + self.heap2[0]) / 2
        return self.heap2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()