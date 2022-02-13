class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start value
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        # Check if tehre is overlap in consecutive intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            # Merge if overlap
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output