class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # (numRows - 1) * 2 elements to travel for one element to next element in same row for first row and bottom row
        if numRows == 1:
            return s
        
        res = ""
        increment = 2 * (numRows - 1)
        
        for r in range(numRows):
            for i in range(r, len(s), increment):
                # Row at first and last
                res += s[i]
                # Rows in between first and last row
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res