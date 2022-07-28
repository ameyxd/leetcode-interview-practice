class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0
        ROWS, COLS = len(board), len(board[0])
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                return
            board[r][c] = 'T' # mark nodes that are adjacent to border nodes
            for dr, dc in steps:
                newr, newc = r + dr, c + dc
                dfs(newr, newc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1):
                    if board[r][c] == 'O':
                        dfs(r, c)
                        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        return board
        