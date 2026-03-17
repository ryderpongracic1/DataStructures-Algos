class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # nums from left to mid is sorted
                if nums[left] <= target < nums[mid]:
                    # target in nums[left, mid]
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # nums[left] > nums[mid]
                # nums from [mid, right] is sorted
                if nums[mid] < target <= nums[right]:
                    # target in range nums[mid, right]
                    left = mid + 1
                else:
                    right = mid - 1
        return -1