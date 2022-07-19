class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # if new interval goes before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if new interval goes after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # there is overlap
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),
                               max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res