class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS, COLS = n, n
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        res = []
        board = [["."] * n for i in range(n)]
        
        
        
        # Index of number in colPlacements tells us the row
        res = []
                
        def backtrack(r):
            # base case: goal
            if r == ROWS:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            else:
                for c in range(COLS):
                    # Validate
                    if c in col or (r + c) in posDiag or (r - c) in negDiag: # Skip, you cannot use this position
                        continue
                    # Choose
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"
                    
                    # Explore
                    backtrack(r + 1)

                    # Unchoose
                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
        
        backtrack(0)
        
        return res