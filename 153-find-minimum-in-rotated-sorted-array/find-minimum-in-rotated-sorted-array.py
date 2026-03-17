class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # mid is of the rotated greater subarray
                # smallest val to the right
                left = mid + 1
            elif nums[mid] <= nums[right]:
                # mid fromn nums mid to right is sorted
                right = mid
        return nums[left]