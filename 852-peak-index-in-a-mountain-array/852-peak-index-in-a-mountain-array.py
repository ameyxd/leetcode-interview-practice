class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # O(n) solution
#         for i in range(len(arr)):
#             if arr[i] > arr[i + 1]:
#                 return arr[i]
        
        # O(logn) solution using binary search
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left