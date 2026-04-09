class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = 0
        least = float('inf')
        for right in range(len(prices)):
            while left < right and prices[left] > prices[right]:
                left += 1

            profit = prices[right] - prices[left]
            if profit > ans:
                ans = profit
        return ans