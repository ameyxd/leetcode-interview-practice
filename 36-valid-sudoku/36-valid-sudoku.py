class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # For each row, column and square: Have a hashset
        # Time: O(1)
        # Key - col number, value - set of all numbers in the column
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = row/3, col/3
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c // 3)]: # dupes found
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True