class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use max heap for finding most frequent task, and queue
        time = 0
        count = collections.Counter(tasks)
        
        # Minheap with neg values is maxheap
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque() # pairs of [-cnt, idleTime(what time will that task be available to process)]
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # Processing the most frequent task (add 1 because negative values, -3A -> -2A)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time