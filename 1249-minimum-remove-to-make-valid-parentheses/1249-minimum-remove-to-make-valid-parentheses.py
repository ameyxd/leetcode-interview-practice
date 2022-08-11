class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # (, ) or string
        stack = [] # Stores indices of open parentheses to remove
        N = len(s)
        res = list(s) # Start with a copy of the list
        
        for i in range(N):
            if res[i] == "(":
                stack.append(i)
            elif res[i] == ")":
                if stack: # there is a matching open parenthesis, so pop that open parenthesis from stack, since you don't want to remove that parenthesis from the string
                    stack.pop()
                else: # this closed parenthesis does not have a valid open parenthesis
                    res[i] = "" # you want to remove the extra close parenthesis from the result
        
        # Stack should contain all the indices of the extra ( that need to be popped
        for j in stack:
            res[j] = "" # Remove the open parenthesis
        
        return "".join(res)