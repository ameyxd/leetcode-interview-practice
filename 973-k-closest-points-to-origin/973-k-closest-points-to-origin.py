class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # no need to take square root for distance, just need squares to compare
        minHeap = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y]) # first would be the key value for heap
        
        heapq.heapify(minHeap)
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res