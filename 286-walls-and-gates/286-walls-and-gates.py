class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # start from gates, BFS to get to each node that is empty. Current node's value will be the node on the prev path's value + 1
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                            
        while queue:
            r, c = queue.popleft()
            for dr, dc in steps:
                newr, newc = r + dr, c + dc
                if newr in range(ROWS) and newc in range(COLS) and rooms[newr][newc] == 2**31 - 1:
                    rooms[newr][newc] = rooms[r][c] + 1
                    queue.append((newr, newc))
        return rooms