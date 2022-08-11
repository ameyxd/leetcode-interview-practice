class RandomizedSet:

    def __init__(self):
        self.data = []
        self.datamap = {}

    def insert(self, val: int) -> bool:
        if val in self.datamap:
            return False
        self.datamap[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.datamap:
            return False
        # Order of the remaining elements doesn't matter
        el_idx, last = self.datamap[val], self.data[-1]
        
        if el_idx < len(self.data) - 1: # make sure you're not at the last element
            self.data[el_idx] = last
            self.datamap[last] = el_idx
        
        self.data.pop()
        del self.datamap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()