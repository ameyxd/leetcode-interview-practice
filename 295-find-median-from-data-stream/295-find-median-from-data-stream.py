class MedianFinder:

    def __init__(self):
        # two heaps: large (minHeap) and small (maxHeap), both heaps should be almost equal size (diff 1)
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # make sure every num in small is <= every num in large
        if (self.small and self.large and ((-1 * self.small[0]) > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # uneven size: Move from small to large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1: # move from large to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()