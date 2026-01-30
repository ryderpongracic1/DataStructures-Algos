class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        curr = 0
        count = 0
        for num in nums:
            curr += num
            if curr == 0:
                count += 1
        return count 