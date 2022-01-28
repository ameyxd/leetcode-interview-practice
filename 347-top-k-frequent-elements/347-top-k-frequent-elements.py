from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count_dict = Counter(nums)
        heap = []
        result = []
        
        # Default heap is minheap: convert to maxheap by storing negative of the keys
        # Step 1: Push into maxheap all the elements - one better way would be to maintain min heap
        for num, count in count_dict.items():
            heapq.heappush(heap, (-count, num))

        result = []
        
        for _ in range(k):
            temp = heapq.heappop(heap)
            result.append(temp[1])
            
        return result