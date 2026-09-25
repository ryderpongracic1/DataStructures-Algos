from collections import defaultdict
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = {}, {} # val -> r, val -> c

        for r in range(m):
            for c in range(n):
                rows[mat[r][c]] = r
                cols[mat[r][c]] = c

        r_count, c_count = defaultdict(int), defaultdict(int) # r -> count
        for i in range(len(arr)):
            num = arr[i]
            row, col = rows[num], cols[num]
            r_count[row] += 1
            c_count[col] += 1
            if r_count[row] == n or c_count[col] == m:
                return i
        