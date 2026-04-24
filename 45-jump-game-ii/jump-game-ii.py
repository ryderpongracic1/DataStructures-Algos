class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps = farthest = end = 0

        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest
                if end >= len(nums) - 1:
                    break
        return jumps