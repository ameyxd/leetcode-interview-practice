class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # start from gates, BFS to get to each node that is empty. Current node's value will be the node on the prev path's value + 1
        # Populate queue and see how each gate's is not fully explored before moving on to the next gate, since each gate only looks at areas within one space of it. So these one space away rooms are marked and added to queue, and so on. Once all gates are checked, each new space in the queue is checked, and so on, so when a room is reached, it has to be from the closest gate. This guarantees that we get the distance from the closest gate.
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