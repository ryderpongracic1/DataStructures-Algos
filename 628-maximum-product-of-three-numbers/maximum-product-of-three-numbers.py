class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # A = max1 * max2 * max 3
        # OR B = min1 * min2 * max1
        # = max(A, B)
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            # get max vals
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            # get min vals
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        res = max(max1 * max2 * max3, max1 * min1 * min2)
        return res
