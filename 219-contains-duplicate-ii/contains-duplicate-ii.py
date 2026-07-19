class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                seen.remove(nums[left])
                left += 1
            if nums[right] in seen:
                return True
            seen.add(nums[right])
        return False