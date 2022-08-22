class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [n for n in nums]
        heapq.heapify(heap)
        while len(heap) > 2:
            heapq.heappop(heap)
            
        return (heap[0] - 1) * (heap[1] - 1)