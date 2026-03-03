class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        total = left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0
        else:
            return ans