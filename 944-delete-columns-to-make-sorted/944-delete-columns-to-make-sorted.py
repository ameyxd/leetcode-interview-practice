class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ROWS, COLS = len(strs), len(strs[0])
        count = 0
        for i in range(COLS):
            for j in range(ROWS - 1):
                if strs[j + 1][i] < strs[j][i]:
                    count += 1
                    break
        return count