class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        def backtrack(row, col, idx):
            if idx == len(word):
                return True
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS):
                return False
            if board[row][col] != word[idx]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'

            down = backtrack(row + 1, col, idx + 1)
            up = backtrack(row - 1, col, idx + 1)
            right = backtrack(row, col + 1, idx + 1)
            left = backtrack(row, col - 1, idx + 1)

            board[row][col] = temp

            return right or left or up or down

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False