class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for price in prices[1:]:
            if price < buy:
                buy = price
            ans = max(ans, price - buy)

        return ans