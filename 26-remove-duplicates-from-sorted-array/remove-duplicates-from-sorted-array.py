class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        idx = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[idx] = nums[i]
                idx += 1
            seen.add(nums[i])

        return len(seen)