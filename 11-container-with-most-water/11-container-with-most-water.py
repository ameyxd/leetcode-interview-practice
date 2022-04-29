class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use two pointers and update them based on the condition
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else: # if equal any pointer can be moved
                r -= 1
        return res