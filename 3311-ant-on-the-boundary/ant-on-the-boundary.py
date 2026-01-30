class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        total = nums[0]
        count = 0
        for i in range(1, len(nums)):
            total += nums[i]
            if total == 0:
                count += 1
        return count 