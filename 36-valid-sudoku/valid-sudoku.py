class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ROWS
        for row in board:
            seen = set()
            for num in row:
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        # COLS
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[j][i]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        # SQUARE
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    num = board[row][col]
                    if num == '.':
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
        return True