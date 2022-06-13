class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use minheap to simulate max heap -> convert all numbers to negative numbers
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if second > first: # actually second less than first but we are using negative values so reverse sign
                heapq.heappush(stones, first - second)
        
        stones.append(0) # If no stones exist, return 0
        
        return abs(stones[0])