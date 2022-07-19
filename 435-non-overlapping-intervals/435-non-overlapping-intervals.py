class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy approach to finding max
        intervals.sort(key=lambda i: i[0])
        minIntervals = 0
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start < lastEnd: # overlap
                minIntervals += 1
                output[-1][1] = min(lastEnd, end) # since smaller one of the two will have lesser chance of overlap with other intervals
            else:
                output.append([start, end])
        return minIntervals