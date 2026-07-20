'''
m = (y2 - y1) / (x2 - x1)
For 2 points: (yi - y0) / (xi - x0) = (y1 - y0) / (x1 - x0)
    => (yi - y0) * (x1 - x0) = (y1 - y0) * (x1 - x0)
    dx = (x1 - x0), dy = (y1 - y0)
    -> (yi - y0) * dx = dy * (xi - x0)

'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0

        for xi, yi in coordinates[1:]:
            if (yi - y0) * dx != dy * (xi - x0):
                return False

        return True