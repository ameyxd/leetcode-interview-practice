class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        flipMap = {"6": "9", "0": "0", "9": "6", "1": "1", "8": "8"}
        flippedNum = ""
        for c in num:
            if c not in flipMap:
                return False
            flippedNum += flipMap[c]
        return flippedNum[::-1] == num