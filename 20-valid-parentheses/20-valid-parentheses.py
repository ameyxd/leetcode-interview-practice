class Solution:
    def isValid(self, s: str) -> bool:
        d = {'}': '{', ']': '[', ')':'('}
        
        stack = []
        for bracket in s:
            if bracket in d.values(): #opening bracket
                stack.append(bracket)
            elif bracket in d.keys(): # If it is a closed bracket, pop from stack and compare
                curr_open = stack.pop() if stack else "%"
                if d[bracket] != curr_open:
                    return False
        if len(stack) == 0:
            return True
