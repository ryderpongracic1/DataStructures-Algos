import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # stores k largest nums, top has kth largest
        self.min_heap = nums[:self.k] # pop when new val is larger than top
        heapq.heapify(self.min_heap)

        for num in nums[self.k:]:
            if num > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)