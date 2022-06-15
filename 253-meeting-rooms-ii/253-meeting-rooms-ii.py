class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        # Min number of conference rooms required = maximum number of overlapping intervals
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        print(start, end)
        res, count = 0, 0
        # Two pointers to traverse through start and end array
        s, e = 0, 0
        while s < len(intervals): # while loop because we only need to worry about meetings starting to keep count of # conference rooms required
            if start[s] < end[e]: # first meeting begins before another ends
                s += 1
                count += 1
            else:
                e += 1
                count -= 1 # A meeting ended before another could start -> reduce # conference rooms needed
            res = max(res, count)
        return res
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Another approach: min-heap that helps keep track of when the earliest meeting ends
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i[0])
        free_rooms = []
        
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]: # if the earliest ending meeting is ending before current event starts
                heapq.heappop(free_rooms) # assign to current meeting
            heapq.heappush(free_rooms, i[1]) # add current room's end time to heap
            
        return len(free_rooms)