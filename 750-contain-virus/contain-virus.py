class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        ROWS, COLS = len(isInfected), len(isInfected[0])
        cardinal = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        while True:
            visited = set()
            clusters = []
            def dfs(r, c, cluster, threat):
                walls = 0

                for dr, dc in cardinal:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            cluster.add((nr, nc))
                            walls += dfs(nr, nc, cluster, threat)
                        elif isInfected[nr][nc] == 0:
                            threat.add((nr, nc))
                            walls += 1
                return walls

            for r in range(ROWS):
                for c in range(COLS):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        cluster = {(r, c)}
                        threat = set()
                        visited.add((r, c))
                        walls = dfs(r, c, cluster, threat)
                        if threat:
                            clusters.append((threat, cluster, walls))
            if not clusters:
                break
            clusters.sort(key=lambda x: len(x[0]))
            threatened, quarantined, building = clusters.pop()
            res += building
            
            for r, c in quarantined:
                isInfected[r][c] = -1
            for remaining, _, _ in clusters:
                for r, c in remaining:
                    isInfected[r][c] = 1
        return res