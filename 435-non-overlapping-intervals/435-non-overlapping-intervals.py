class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        # intervals.sort()
        res = 0
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # Non-overlapping
            if start >= lastEnd:
                lastEnd = end # Update end time
            # There is overlap -> one of the intervals amongst the current interval and the previous interval needs to be removed
            # Decide which interval to remove based on which interval ends first - since that reduces chances of intervals after it overlapping with it, i.e., shorter the interval, the better, so keep the shorter, i.e.m one that ends first
            else:
                res += 1 # Number of intervals to be deleted
                lastEnd = min(end, lastEnd) # erase one with largetr end time
        return res
    