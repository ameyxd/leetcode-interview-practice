class Solution:
    def maxAreaOfIsland_rec(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        maxArea = 0
        
        
        def dfs(r, c):
            if not r in range(rows) or not c in range(cols) or not grid[r][c] == 1:
                return 0
            grid[r][c] = 0
            area = 0
            for dr, dc in steps:
                newr, newc = r + dr, c + dc
                area += dfs(newr, newc)
            return area + 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    m = dfs(row, col)
                    maxArea = max(m, maxArea)
        return maxArea
    
    # Iterative DFS solution
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        maxArea = 0
        
        def dfs_iterative(row, col):
            area = 0
            stack = [(row, col)]
            visited.add((row, col))
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in steps:
                    newr, newc = r + dr, c + dc
                    if (newr, newc) not in visited and newr in range(rows) and newc in range(cols) and grid[newr][newc] == 1:
                        stack.append((newr, newc))
                        visited.add((newr, newc))
            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs_iterative(row, col)
                    maxArea = max(area, maxArea)
        return maxArea