class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')
        left = 0
        for right in range(len(nums)):
            subarray = prefix[right + 1] - prefix[left]
            while subarray >= target:
                ans = min(ans, right - left + 1)
                left += 1
                subarray = prefix[right + 1] - prefix[left]

        if ans == float('inf'):
            return 0
        else:
            return ans