class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            # if num - 1 in nums: num CANNOT be starting point of longest
            if num - 1 not in nums:
                i = 1
                while num + i in nums:
                    i += 1
                res = max(res, i)
        return res