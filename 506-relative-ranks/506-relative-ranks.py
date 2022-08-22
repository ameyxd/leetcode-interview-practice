class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Build maxheap
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)
        
        output = [0] * len(score)
        rank = 1

        while heap:
            score, i = heapq.heappop(heap)
            if rank == 1:
                output[i] = "Gold Medal"
            elif rank == 2:
                output[i] = "Silver Medal"
            elif rank == 3:
                output[i] = "Bronze Medal"
            else:
                output[i] = str(rank)
            rank += 1
        return output