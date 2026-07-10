### NOTES
# - BFS: expand out from each rotten orange as a wave
# - Track minute incrementing as rotten orages expand as a wave
# - Track count of fresh oranges seen
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque() # BFS - (r, c) of rotten fruit
        minutes = 0
        numFresh = 0 # num of fresh oranges seen
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)] # cardinal directions
        while queue and numFresh > 0: # only run if fresh oranges remain
            numRotten = len(queue)
            for _ in range(numRotten):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS:
                        continue
                    # grid[newR][newC] won't throw IndexOutOfBounds
                    if grid[newR][newC] == 1:
                        # fresh fruit at (newR, newC) will be contaminated
                        numFresh -= 1
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
            minutes += 1
        if numFresh > 0:
            return -1
        return minutes
