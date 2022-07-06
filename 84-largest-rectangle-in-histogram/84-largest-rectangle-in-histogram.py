class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # If heights aren't in increasing order they will be popped since they cannot be 'extended' to the right
        # Only popping from most recent elements, so stack
        maxArea = 0
        stack = [] # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # top values height is greater than height we reached
                # pop and check area
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        # For heights left in stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea