from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # Solution 1: Using Heap O(k log n)
#         if k == len(nums):
#             return nums
        
#         count_dict = Counter(nums)
#         heap = []
#         result = []
        
#         # Default heap is minheap: convert to maxheap by storing negative of the keys
#         # Step 1: Push into maxheap all the elements - one better way would be to maintain min heap
#         for num, count in count_dict.items():
#             heapq.heappush(heap, (-count, num))

#         result = []
        
#         for _ in range(k):
#             temp = heapq.heappop(heap)
#             result.append(temp[1])
            
#         return result

        # Solution 2: Using bucket sort like array storing list of values that have a particular count at count position: O(n)
    
        # Step 1: Make freq list of lists
        freq = [[] for i in range(len(nums) + 1)] # Map all nums to the index of the number of times they occur using count_dict
        count_dict = collections.Counter(nums)
        
        for num, count in count_dict.items():
            freq[count].append(num)

        # Step 2: Start from the end and traverse to the start populating res with the top k most frequently occuring elements and break when res is full, i.e., at length k 
        res = []
        # Start from the end of the freq list and get the top k most frequent elements        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
    