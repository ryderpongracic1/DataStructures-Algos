class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevLeast = prices[0]
        ans = 0
        for i in range(len(prices)):
            prevLeast = min(prevLeast, prices[i])
            ans = max(ans, prices[i] - prevLeast)
        return ans