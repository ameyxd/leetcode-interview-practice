class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        maxHeight = heights[-1]
        if len(heights) == 1:
            return res
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                res.append(i)
        return res[::-1]