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
            if len(heap) < k: # First k elements
                heapq.heappush(heap, (freq, num))
            else: # Only keep k greatest
                heapq.heappushpop(heap,(freq, num))
        
        for freq, num in heap:
            ans.append(num)
        return ans