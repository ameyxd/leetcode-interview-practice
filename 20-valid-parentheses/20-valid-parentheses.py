class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}": "{", ")" : "(", "]" : "["}
        
        stack = []
        for bracket in s:
            # if it is an open bracket, put into stack
            if bracket in d.values():
                stack.append(bracket)
            # If it is a closed bracket, pop from stack and compare
            elif bracket in d.keys():
                curr_open_bracket = stack.pop() if stack else "$"
                if curr_open_bracket != d[bracket]:
                    return False
        if len(stack) == 0:
            return True