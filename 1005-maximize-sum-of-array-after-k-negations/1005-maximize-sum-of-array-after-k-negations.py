class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
         # Greedily flip number with smallest value
        heapq.heapify(nums)
        for i in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, -1 * num)
        
        return sum(nums)