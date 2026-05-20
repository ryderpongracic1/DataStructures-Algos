import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        min_heap = [(nums1[0] + nums2[0], 0, 0)] # sum, idx1, idx2
        seen = set() # idx1, idx2
        while min_heap and len(res) < k:
            val, idx1, idx2 = heapq.heappop(min_heap)
            if (idx1, idx2) in seen:
                continue
            seen.add((idx1, idx2))
            res.append((nums1[idx1], nums2[idx2]))
            if idx1 < len(nums1) - 1:
                heapq.heappush(min_heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
            if idx2 < len(nums2) - 1:
                heapq.heappush(min_heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
        return res