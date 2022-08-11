class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows, cols, squares = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        
        def populate():
            for r in range(n):
                for c in range(n):
                    if board[r][c] == '.':
                        continue
                    v = int(board[r][c])
                    rows[r].add(v)
                    cols[c].add(v)
                    squares[(r // 3, c // 3)].add(v)
        
        def isValid(r, c, v):
            return (v not in rows[r]) and (v not in cols[c]) and (v not in squares[(r // 3, c // 3)])
        
        def placeNum(r, c, v):
            board[r][c] = str(v)
            rows[r].add(v)
            cols[c].add(v)
            squares[(r // 3, c // 3)].add(v)
        
        def removeNum(r, c, v):
            board[r][c] = '.'
            rows[r].remove(v)
            cols[c].remove(v)
            squares[(r // 3, c // 3)].remove(v)
        
        def getNextCell(r, c):
            if c < 8:
                nr, nc = r, c + 1
            else:
                nr, nc = r + 1, 0
            return nr, nc
        
        def backtrack(r, c):
            if r == n - 1 and c == n:
                # print(board)
                return True
            elif c == n:
                c, r = 0, r + 1
            
            # print(r, c)
            if board[r][c] != '.':
                return backtrack(r, c + 1)
            # else:
            for val in range(1, 10):
                if isValid(r, c, val):
                    placeNum(r, c, val)
                    if backtrack(r, c + 1):
                        return True
                    removeNum(r, c, val)
            return False
        populate()
        backtrack(0, 0)