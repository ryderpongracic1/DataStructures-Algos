class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0 # where next non-val goes / last spotted 2
        for i in range(len(nums)):
            if nums[i] != val: # i is a non-val -> place at last spotted 2
                nums[idx] = nums[i]
                idx += 1
        return idx