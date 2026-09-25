class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        n = len(row)
        pos = {p: i for i, p in enumerate(row)}
        res = 0

        for i in range(0, len(row), 2):
            p1 = row[i]
            expected = p1 ^ 1
            p2 = row[i + 1]
            
            if p2 != expected:
                p2idx = pos[expected]
                row[i + 1], row[p2idx] = row[p2idx], row[i + 1]
                pos[p2] = p2idx
                res += 1
        return res