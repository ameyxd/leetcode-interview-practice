class Solution:
    def trap1(self, height: List[int]) -> int:
        
        # Strat: maintain the max height to the left and right of any point i and use the min of those two to calculate water trapped
        
        maxLeft, maxRight = [0] * len(height), [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(height[i + 1], maxRight[i + 1])
        
        res = 0
        for i in range(len(height)):
            waterAti = min(maxLeft[i], maxRight[i]) - height[i]
            if waterAti > 0:
                res += waterAti
        return 
    
    def trap(self, height: List[int]) -> int:
        # O(1) memory solution
        # Strat: maintain the max height to the left and right of any point i and use the min of those two to calculate water trapped
        # Use two pointers
        
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        res = 0
        
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left] # since maxLeft is being updated before this, no need to check if maxLeft - height[left] > 0 or not
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
            
        return res