class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # next permutation is the smallest larger num
        # find least-significant digit (R->L) s.t. nums[i] < nums[i + 1]
        # e.g. 
        # 1 4 7 5 4 3 1 -> subarray [75431] in max lexicographic arrangement
        # 4 < 7 so pivot is 4
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # pivot = i

        # i = -1 means nums already in greatest arrangement (e.g. 5,3,2,1):
        #   reverse entire array
        # i >= 0 means pivot = i:
        #   swap pivot & smallest num larger than pivot in subarray
        if i >= 0:  
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse subarray after pivot so that the rest of the num is smallest
        # if pivot = -1, reverse entire array
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1