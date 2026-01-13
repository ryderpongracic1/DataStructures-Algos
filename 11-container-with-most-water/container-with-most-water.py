class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = 0

        while left < right:
            container = (right - left) * min(height[right], height[left])
            maxWater = max(maxWater, container)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxWater