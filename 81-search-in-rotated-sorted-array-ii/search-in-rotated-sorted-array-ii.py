class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] == nums[right]:
                # move duplicates
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]:
                # nums from [left, mid] is sorted
                if nums[left] <= target < nums[mid]:
                # target in nums from [left, mid]
                    right = mid - 1
                else:
                    # target not in this subarray
                    left = mid + 1
            elif nums[mid] <= nums[left]:
                # nums from [mid, right] is sorted
                if nums[mid] < target <= nums[right]:
                    # target in nums from [mid, right]
                    left = mid + 1
                else:
                    right = mid - 1
        return False