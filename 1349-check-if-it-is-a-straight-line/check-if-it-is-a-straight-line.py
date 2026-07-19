"""
m = (y2 - y1) / (x2 - x1)
=> ((yi - y0) / (xi - x0)) = ((y2 - y1) / (x2 - x1))
=> (y2 - y0) * (x2 - x1) = (y2 - y1) * (xi - x0)
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0][0], coordinates[0][1]
        for i in range(1, len(coordinates)):
            x2, y2 = coordinates[i][0], coordinates[i][1]
            x1, y1 = coordinates[i - 1][0], coordinates[i - 1][1]
            if (y2 - y0) * (x2 - x1) != (y2 - y1) * (x2 - x0):
                return False
        return True