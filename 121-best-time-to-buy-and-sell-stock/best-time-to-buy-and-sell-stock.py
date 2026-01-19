class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right in range(len(prices)):
            curr = prices[right] - prices[left]
            profit = max(profit, curr)
            while left < right and prices[left] > prices[right]:
                left += 1
        return profit