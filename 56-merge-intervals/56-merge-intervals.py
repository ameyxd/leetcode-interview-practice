class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]
        # Remember lastEnd
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            # Overlap
            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            # No overlap
            else:
                res.append([start, end])
        
        return res