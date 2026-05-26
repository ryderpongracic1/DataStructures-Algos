class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # trackers for placed queens
        cols = set()
        # r + c is constant across positive diagonals
        pos_diag = set()
        # r - c is constant across negative diagonals
        neg_diag = set()

        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            # placed queen in each n rows 
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            # horizontally traverse tree for choosing a col per row
            for c in range(n):
                # prune unsafe branches
                if c in cols or r + c in pos_diag or r - c in neg_diag:
                    continue
                # place queen & mark sets
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                dfs(r + 1) # explore

                # backtrack for future branches
                board[r][c] = '.'
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        dfs(0)
        return res