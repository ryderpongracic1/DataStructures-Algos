from collections import defaultdict
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowCount = [0] * m # row r -> how many cells in row r been painted
        colCount = [0] * n # col c -> how many cells in col c been painted

        coordMap = [0] * (m * n + 1) # val -> (r, c)
        for r in range(m):
            for c in range(n):
                coordMap[mat[r][c]] = (r, c)
        
        for i in range(len(arr)):
            r, c = coordMap[arr[i]]
            rowCount[r] += 1
            colCount[c] += 1
            print(r)
            if rowCount[r] >= n or colCount[c] >= m:
                return i