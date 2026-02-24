class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0:1}
        ans = total = 0
        for num in nums:
            total += num
            if total - k in prefix_counts:
                ans += prefix_counts[total - k]
            prefix_counts[total] = prefix_counts.get(total, 0) + 1
        return ans