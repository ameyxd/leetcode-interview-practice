class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        # make two arrays for start and end times use two pointers to traverse start and end arrays
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count, res = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            # New room required
            if start[s] < end[e]:
                s += 1
                count += 1
            
            # Room emptied, meeting complete
            else:
                e += 1
                count -= 1
            res = max(count, res)
        return res
    
    # Min heap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        endTimeHeap = []
        heapq.heappush(endTimeHeap, intervals[0][1])
        
        for i in intervals[1:]:
            # of all occupied rooms, if the earliest ending meeting ends before current meeting starts
            if endTimeHeap[0] <= i[0]:
                heapq.heappop(endTimeHeap)
            heapq.heappush(endTimeHeap, i[1])
        
        return len(endTimeHeap)