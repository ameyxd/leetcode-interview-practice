class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
		# Directions we'll use to change our location (down, up, right, left).
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # We'll use a deque for our BFS traversal.
        q = collections.deque([])
		# Append our starting details to the q.
		# (row, col, steps, k)
        q.append((0, 0, 0, k))
		# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
        seen = set()
        while q:
		    # Pop the next location from the q.
            r, c, steps, rk = q.popleft()
			# If we're at the finish location return the steps, given BFS this will be
			# guaranteed to be the first to hit this condition.
            if r == rows-1 and c == cols - 1:
                return steps
			# Otherwise we'll keep travelling throught the grid in our 4 directions.
            else:
                for y, x in directions:
                    nr = r + y
                    nc = c + x
					# If the new location is on the board and has not been visited.
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc, rk) not in seen:
					    # If it's a blocker but we still have k left, we'll go there and k -= 1.
                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))
						# Otherwise continue on  if it's a 0 - free location.
                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk))
		# If we don't hit the end in our traversal we know it's not possible.
        return -1
    def shortestPath1(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = collections.deque([(0, 0, k, 0)])
        visited = set((0, 0, k))
        path = 0
        while queue:
            r, c, nk, path = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return path
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc, nk) not in visited:
                    if grid[nr][nc] == 1 and nk > 0:
                        queue.append((nr, nc, nk - 1, path + 1))
                        visited.add((nr, nc, nk - 1))
                    elif grid[nr][nc] == 0:
                        queue.append((nr, nc, nk, path + 1))
                        visited.add((nr, nc, nk))
        print(path)
        return -1