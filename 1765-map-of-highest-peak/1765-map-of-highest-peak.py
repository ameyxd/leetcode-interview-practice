class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heights = [[-1] * COLS for _ in range(ROWS)]
        
        queue = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    heights[r][c] = 0
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] == -1:
                    heights[nr][nc] = heights[r][c] + 1
                    queue.append((nr, nc))
                    
        return heights