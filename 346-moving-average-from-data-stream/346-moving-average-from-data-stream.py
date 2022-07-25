class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list = []
        self.curr = 0

    def next(self, val: int) -> float:
        if self.curr < self.size:
            self.list.append(val)
            self.curr += 1
            return sum(self.list)/self.curr
        else:
            self.list.pop(0)
            self.list.append(val)
            return sum(self.list)/self.size
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)