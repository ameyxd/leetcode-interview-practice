class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # push into stack until you see ]
        # Start decoding the string
        # pop from stack, get n, add string n times to result
        
        for char in s:
            if char == ']':
                # start decoding
                currString = []
                # while you read a alphabetical char, add to current string
                while stack[-1] != "[":
                    currChar = stack.pop()
                    currString.append(currChar)
                stack.pop() # this will be the [
                num, k = 0, 0
                while stack and stack[-1].isdigit():
                    print(stack[-1])
                    dig = int(stack.pop())
                    num += dig * 10**k
                    k += 1
                # push back into stack in reverse order num times
                for _ in range(num):
                    for i in range(len(currString) - 1, -1, -1):
                        stack.append(currString[i])
            else:
                # push char into stack
                stack.append(char)
        return ("".join(stack))