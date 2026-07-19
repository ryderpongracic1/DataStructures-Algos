"""
m = (y2 - y1) / (x2 - x1)
=> ((yi - y0) / (xi - x0)) = ((y2 - y1) / (x2 - x1))
=> (y2 - y0) * (x2 - x1) = (y2 - y1) * (xi - x0)

diff between first 2 pts: dx = x1 - x0, dy = y1 - y0
for pt i, check: dy * (xi - x0) == (yi - y0) * dy
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if dy * (xi - x0) != (yi - y0) * dx:
                return False
        return True