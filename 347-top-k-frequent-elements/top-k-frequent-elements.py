import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        ans = []
        for num in nums:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1

        heap = []
        for num, freq in elements.items():
            # Add elements to heap to keep greatest
            heapq.heappush(heap, (freq, num))
            if len(heap) > k: # Only keep k greatest
                heapq.heappop(heap)
        
        for freq, num in heap:
            ans.append(num)
        return ans