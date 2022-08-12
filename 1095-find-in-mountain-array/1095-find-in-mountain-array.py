# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # If you find the peak, you can do binary search on the two parts separately
        # Binary search to find the peak
        def findPeak(l, r):
            # while l < r:
            #     mid = l + (r - l) // 2
            #     if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
            #         l = mid + 1
            #     else:
            #         r = mid
            # return l
            while l < r:
                mid = l + (r - l) // 2
                val = mountain_arr.get(mid)
                if 0 < mid < mountain_arr.length():
                    valLeft = mountain_arr.get(mid - 1)
                    valRight = mountain_arr.get(mid + 1)
                    if val < valRight:
                        l = mid + 1
                    elif valLeft > val > valRight:
                        r = mid
                    else:# Found peak
                        return mid
            
        def binarySearch1(l, r, target):
            while l < r:
                mid = l + (r - l) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    l = mid + 1
                else:
                    r = mid
            if mountain_arr.get(l) == target:
                return l
            return -1
        
        def binarySearch2(l, r, target):
            while l < r:
                mid = l + (r - l) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    l = mid + 1
                else:
                    r = mid
            if mountain_arr.get(l) == target:
                return l
            return -1
        
        l, r = 0, mountain_arr.length() - 1
        peak = findPeak(l, r)
        leftidx = binarySearch1(l, peak, target)
        if leftidx > 0:
            return leftidx
        else:
            rightidx = binarySearch2(peak, r, target)
        if leftidx < 0 and rightidx < 0:
            return -1
        if leftidx < 0 or rightidx < 0:
            return max(leftidx, rightidx)
        else:
            return min(leftidx, rightidx)