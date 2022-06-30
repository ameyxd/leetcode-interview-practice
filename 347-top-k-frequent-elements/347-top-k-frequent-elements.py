class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
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
        for num, count in countDict.items():
            heapq.heappush(heap, (-count, num))
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n): Bucket sort like - need values to be in a range as a condition on input
        # Make hashmap of frequency, then make a list, where at index i store the value that occurs i times
        if k == len(nums):
            return nums
    
        countDict = Counter(nums)
        heap, res = [], []
        bucket_list = [[] for _ in range(len(nums) + 1)]
        for num, count in countDict.items():
            bucket_list[count].append(num)
        flattened_list = [item for sublist in bucket_list for item in sublist]
        # Go in reverse order since most frequent element will be last
        return flattened_list[::-1][:k]
    
