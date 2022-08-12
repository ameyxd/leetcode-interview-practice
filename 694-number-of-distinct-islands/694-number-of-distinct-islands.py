class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        uniqueIslands = set()
        dirs = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
        visited = set()
        
        def dfs(r, c, direction):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or not grid[r][c]:
                return
                        
            path.append(direction)
            # for d in dirs:
            #     dr, dc = dirs[d][0], dirs[d][1]
            #     nr, nc = r + dr, c + dc
            #     # if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] == 1:
            visited.add((r, c))
            #     dfs(nr, nc, d)
            dfs(r + 1, c, "D")
            dfs(r - 1, c, "U")
            dfs(r, c + 1, "R")
            dfs(r, c - 1, "L")
            path.append("0")
            
        for r in range(ROWS):
            for c in range(COLS):
                path = []
                dfs(r, c, "0")
                print(path)
                if path:
                    uniqueIslands.add(tuple(path))
        print(uniqueIslands)            
        return len(uniqueIslands)