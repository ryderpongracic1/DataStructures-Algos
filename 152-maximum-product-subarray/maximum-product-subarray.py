class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMax = 1
        currMin = 1
        curr = 1
        for num in nums:
            curr = currMax * num
            currMax = max(curr, currMin * num, num)
            currMin = min(curr, currMin * num, num)
            ans = max(ans, currMax)
        return ans