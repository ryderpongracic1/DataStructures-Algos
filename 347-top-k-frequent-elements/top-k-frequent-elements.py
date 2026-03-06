import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, fr in freq.items():
            heapq.heappush(heap, (fr, num))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            ans[i] = heap[i][1]
        return ans