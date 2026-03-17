class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = 0
        for right in range(len(prices)):
            while left < right and prices[right] < prices[left]:
                left += 1
            ans = max(ans, prices[right] - prices[left])
        return ans