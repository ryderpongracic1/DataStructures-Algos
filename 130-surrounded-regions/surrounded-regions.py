# Border cells are safe
# Scan borders for safe 'O' - run DFS looking for connected 'O's
# Mark safe 'O's as visited
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if board[r][c] != 'O':
                return
            board[r][c] = '#' # temp visited marker
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0) # left border
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1) # right border
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c) # top border
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c) # bottom border
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                # don't surround safe cells just changed back to 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
