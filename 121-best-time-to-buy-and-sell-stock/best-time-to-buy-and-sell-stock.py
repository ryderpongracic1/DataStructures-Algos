class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        res = 0
        for p in prices[1:]:
            if p > prev:
                res = max(res, p - prev)
            else:
                prev = p

        return res