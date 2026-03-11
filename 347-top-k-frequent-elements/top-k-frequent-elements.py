import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hset = {}
        for num in nums:
            hset[num] = hset.get(num, 0) + 1

        heap = []
        for num, freq in hset.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
                heapq.heappop(heap)
        ans = [0] * k
        for i in range(k):
            ans[i] = heap[i][1]
        return ans