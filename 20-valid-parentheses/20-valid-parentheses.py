class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {'}':'{', ']':'[', ')':'('}
        stack = []
        
        for char in s:
            if char in parDict.values():
                stack.append(char)
            if char in parDict:
                topStack = stack.pop() if stack else "!"
                if not parDict[char] == topStack:
                    return False

        return len(stack) == 0