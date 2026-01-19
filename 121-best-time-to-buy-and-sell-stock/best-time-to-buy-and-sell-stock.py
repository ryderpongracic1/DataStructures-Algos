class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = left = 0
        ans = 0
        for right in range(len(prices)):
            curr = prices[right] - prices[left]
            while curr < 0:
                left += 1
                curr = prices[right] - prices[left]
            ans = max(ans, prices[right] - prices[left])
            print(left,right,ans)
        return ans