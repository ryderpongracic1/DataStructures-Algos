class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        right = 0
        for left in range(len(nums)):
            if nums[left] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
            # print(i, nums)
                    