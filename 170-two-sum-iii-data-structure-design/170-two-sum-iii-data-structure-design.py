class TwoSum:

    def __init__(self):
        self.num_counts = {}

    def add(self, number: int) -> None:
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value: int) -> bool:
        for num in self.num_counts.keys():
            complement = value - num
            if num != complement:
                if complement in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)