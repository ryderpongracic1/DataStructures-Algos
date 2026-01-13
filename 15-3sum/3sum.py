class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                
                if curr > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else: # curr == 0
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return ans