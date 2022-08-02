class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Time complexity = O(N!) possible positions for the queens
        # Space complexity = O(n), since the maximum recursion depth is n, also the length for all three hashsets.
        ROWS, COLS = n, n
        cols = set()
        posDiag = set() # store (r + c)
        negDiag = set() # store (r - c)
        res = []
        board = [["."] * COLS for i in range(ROWS)]
        
        def backtrack(r):
            # base case: goal reached
            if r == ROWS:
                # append board to result
                copy = ["".join(rows) for rows in board]
                res.append(copy)
                return
            else:
                for c in range(COLS):
                    # Validate
                    if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                        continue
                    # Place
                    cols.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"
                    
                    # Backtrack
                    backtrack(r + 1)
                    
                    # Unplace
                    cols.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
                    
        backtrack(0)
        return res