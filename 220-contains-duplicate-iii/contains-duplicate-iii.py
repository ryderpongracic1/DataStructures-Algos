class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {} 
        k = valueDiff + 1

        for i, num in enumerate(nums):
            bucket_id = num // k
            if bucket_id in buckets:
                return True
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            buckets[bucket_id] = num

            if i >= indexDiff:
                old_id = nums[i - indexDiff] // k
                del buckets[old_id]
        return False