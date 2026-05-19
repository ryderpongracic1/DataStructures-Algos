import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k] # stores top k largest elements
        heapq.heapify(min_heap) # top has kth largest so far

        for num in nums[k:]:
            # new num is larger than kth largest so far
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        # top of min_heap holds kth largest element in nums
        return min_heap[0]