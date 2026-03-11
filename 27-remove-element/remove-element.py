class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
        return writer