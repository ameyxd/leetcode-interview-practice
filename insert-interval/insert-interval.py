class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Find new position for the incoming interval
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # end of new interval is before the start of the current interval
                res.append(newInterval)
                return res + intervals[i:] # intervals after this interval will also be non-overlapping so add them to result as well
            elif newInterval[0] > intervals[i][1]: # new interval goes after current interval
                res.append(intervals[i])
            else: # New interval is overlapping - merge
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # new merged interval may still overlap with intervals after it so don't add to res just yet
        res.append(newInterval)
        return res
    
    
    
    # 3 cases for any new interval to insert it: 
        # 1. new interval goes before the current interval
        # 2. new interval goes after the current interval
        # 3. new interval overlaps - merge new interval