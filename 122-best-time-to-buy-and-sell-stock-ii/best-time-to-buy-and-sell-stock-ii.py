class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        prev = prices[0]
        
        for p in prices[1:]:
            if prev < p:
                ans += p - prev

            prev = p


        return ans