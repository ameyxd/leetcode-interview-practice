class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n log k): Minheap of size k
        if k == len(nums):
            return nums
        countDict = Counter(nums)
        heap, res = [], []
        for num, count in countDict.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [elem[1] for elem in heap]
        
        # for _ in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res
    
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        # O(k log n): Maxheap of size n
        if k == len(nums):
            return nums
    
        countDict = Counter(nums)
        heap, res = [], []
        for count, num in countDict.items():
            heapq.heappush(heap, (-count, num))
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res