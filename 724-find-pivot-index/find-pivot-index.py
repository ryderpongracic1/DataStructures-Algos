class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total, curr = sum(nums), 0
        for i in range(len(nums)):
            if curr == total - curr - nums[i]:
                return i
            curr += nums[i]
        return -1