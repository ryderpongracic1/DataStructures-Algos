class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            left = False
            right = False
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    left = True
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    right = True
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
            if n <= 0:
                return True
        return False