class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count, left = 0, n - 1

        for right in range(n - 1, -1, -1):
            if nums[right] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left -= 1
        
        return left + 1