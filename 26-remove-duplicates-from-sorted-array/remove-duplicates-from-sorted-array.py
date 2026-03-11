class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[k] = nums[i]
                k += 1
            seen.add(nums[i])
        return k