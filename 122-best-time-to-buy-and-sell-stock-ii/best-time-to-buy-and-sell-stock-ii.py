class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]
        for p in prices[1:]:
            if p > curr:
                res += (p - curr)
            curr = p

        return res