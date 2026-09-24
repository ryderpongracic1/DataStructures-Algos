class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def _parse_cell(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        return row - 1, col

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = 0

    def getValue(self, formula: str) -> int:
        X, Y = formula.strip('=').split('+')
        if X[0].isalpha():
            rx, cx = self._parse_cell(X)
            x = self.grid[rx][cx]
        else:
            x = int(X)
        if Y[0].isalpha():
            ry, cy = self._parse_cell(Y)
            y = self.grid[ry][cy]
        else:
            y = int(Y)
        return x + y

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)