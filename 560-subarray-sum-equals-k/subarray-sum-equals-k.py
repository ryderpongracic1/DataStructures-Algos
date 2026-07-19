'''
curr - prefix = k
curr - k = prefix
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        curr, res = 0, 0
        for num in nums:
            curr += num
            if curr - k in prefix:
                res += prefix[curr - k]
            prefix[curr] = prefix.get(curr, 0) + 1
        return res