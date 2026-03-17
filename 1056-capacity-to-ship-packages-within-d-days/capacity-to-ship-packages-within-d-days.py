class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shippable(limit):
            elapsed = 1
            curr = 0
            for w in weights:
                if curr + w > limit:
                    # w cannot go on this ship
                    # it goes on tomorrow's ship
                    elapsed += 1
                    curr = w
                else:
                    curr += w
            return elapsed <= days

        # Search space is from [max(weights), sum(weights)]
        # max(weights) or else the ship will not be able to ever take the heaviest package
        # sum(weights) so the ship can take everything if days = 1
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            if shippable(mid):
                # ship is valid, search for lighter valid ship
                right = mid - 1
            else:
                # ship is too light
                left = mid + 1
        
        # left will store lightest ship that is heavy enough to ship in days
        # right will store heaviest ship that is too light to ship
        return left