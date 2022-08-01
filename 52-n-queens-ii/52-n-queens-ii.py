class Solution:
    def totalNQueens(self, n: int) -> int:
        ROWS, COLS = n, n
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        board = [["."] * ROWS for c in range(COLS)]
        solutions = [0]
        
        def backtrack(r):
            # base case:
            if r == ROWS:
                solutions[0] += 1
                return
            else:
                for c in range(COLS):
                    # validate
                    if c in col or (r + c) in posDiag or (r - c) in negDiag:
                        continue
                    
                    # place queen
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"
                    
                    # backtrack
                    backtrack(r + 1)
                    
                    # remove queen
                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
                    
        backtrack(0)
        return solutions[0]