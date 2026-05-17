import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k] # holds k largest, top is kth largest
        heapq.heapify(min_heap)
        for num in nums[k:]:
            # new num is larger than kth largest
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]