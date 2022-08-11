class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        tmp = [[None] * N for _ in range(M)]
        
        def helper(r, c):
            # Track live neighbors of that cell
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(M) and nc in range(N) and board[nr][nc] == 1:
                    count += 1
            # Apply given conditions
            if board[r][c] == 1:
                if count < 2:
                    return 0
                elif count == 2 or count == 3:
                    return 1
                else:
                    return 0
            else:
                if count == 3:
                    return 1
                else:
                    return 0
            
        # Call helper at all positions
        for r in range(M):
            for c in range(N):
                tmp[r][c] = helper(r, c)
                
        for r in range(M):
            for c in range(N):
                board[r][c] = tmp[r][c]
        
        