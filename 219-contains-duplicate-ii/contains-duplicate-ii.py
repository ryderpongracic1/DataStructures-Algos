class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k == 0:
            return False
        left = 0
        seen = {nums[left] : 1}
        for right in range(1, len(nums)):
            if right - left > k:
                seen[nums[left]] -= 1
                left += 1
            if seen.get(nums[right], 0) > 0:
                return True
            seen[nums[right]] = seen.get(nums[right], 0) + 1
        return False