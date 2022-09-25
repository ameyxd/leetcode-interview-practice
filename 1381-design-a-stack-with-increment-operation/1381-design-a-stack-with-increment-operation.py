class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.stack = []

    def push(self, x: int) -> None:
        # if stack size is less than or equal to maxsize add x to top of stack
        if self.size < self.maxSize:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        # pops and return top of stack, reduce size by 1 or -1 if stack is empty
        # print("HERHERHE")
        if self.size > 0:
            top = self.stack[-1]
            self.stack = self.stack[:-1]
            self.size -= 1
            return top
        return -1
        
    def increment(self, k: int, val: int) -> None:
        # if stack size < k, increment all elements in stack
        if self.size < k:
            self.stack = [x + val for x in self.stack]
        # else bottom k elements incremented by val
        else:
            self.stack = [x + val if i < k else x for i, x in enumerate(self.stack)]