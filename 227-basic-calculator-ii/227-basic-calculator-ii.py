class Solution:
    def calculate(self, s: str) -> int:
        prev_op, val = "+", 0
        stack = []
        for i, x in enumerate(s):
            if x.isdigit(): val = 10*val + int(x)
            if x in "+-*/" or i == len(s) - 1:
                if prev_op == "+": stack.append(val) # insert into the stack
                if prev_op == "-": stack.append(-val) # insert neg value in stack because a - b == a + (-b)
                if prev_op == "*": stack.append(stack.pop() * val) # this operation takes precedence, so pop from stack and calculate before pushing
                if prev_op == "/": stack.append(int(stack.pop() / val)) # same as multiply
                prev_op = x # set new operation for memory
                val = 0 # reset value
        return sum(stack)