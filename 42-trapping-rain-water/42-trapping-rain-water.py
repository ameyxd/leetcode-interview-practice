class Solution:
    def trap(self, height: List[int]) -> int:
        # Get max left and right heights at each position i and get min of that. Subtract that from height at ith position to get water that can be trapped at that position
        # First you can use three lists to store the maxLeft, maxRight and min(maxLeft, maxRight) at each position, the optimize it by using two pointers instead
        if not height: return 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0
        
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l] 
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
            
        return res