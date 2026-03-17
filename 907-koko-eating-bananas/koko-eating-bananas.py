import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def edible(rate):
            elapsed = 0
            for pile in piles:
                elapsed += math.ceil(pile / rate)
            return elapsed <= h
    
        # Search space must be [1, max(piles)]
        # left = 1 because rate of 0 will never finish
        # right = max(piles) as the fastest possible rate
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if edible(mid):
                # this rate finishes the piles within h hours
                # search for a slower valid rate
                right = mid - 1
            else:
                # this rate is too slow to finish the piles
                left = mid + 1
        # left will store the slowest rate that finishes the piles
        # right will store the greatest rate that doesn't finish
        return left