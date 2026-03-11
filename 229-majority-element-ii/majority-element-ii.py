class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        hset = {}
        for num in nums:
            hset[num] = hset.get(num, 0) + 1
        
        for num, freq in hset.items():
            if freq > len(nums) // 3:
                ans.append(num)
        return ans