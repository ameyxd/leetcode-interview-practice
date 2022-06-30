class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check current validity only. not potential validity after filling.
        from collections import defaultdict
        
        rowDict, colDict, squareDict = defaultdict(set), defaultdict(set), defaultdict(set)
        ROWS, COLS = 9, 9
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rowDict[row]) or (board[row][col] in colDict[col]) or (board[row][col] in squareDict[(row // 3, col // 3)]):
                    return False
                rowDict[row].add(board[row][col])
                colDict[col].add(board[row][col])
                squareDict[(row // 3, col // 3)].add(board[row][col])
        return True