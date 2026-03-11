class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                i = 0
                while num + i in nums:
                    i += 1
                ans = max(ans, i)
        return ans