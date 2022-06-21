class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # We don't need the ENTIRE combined array to be sorted, just need to find middle elements
        # If we can partition A at i and B at j such that every element in Aleft and
        # Bleft is less than every element in Aright and Bright,
        # we can get the median from the elements on the sides of the partition boundary
        
        # Binary search on the smaller amongst the two lists. Time complexity O(log(min(A, B)))
        A, B = nums1, nums2
        MAX_INT = sys.maxsize
        MIN_INT = -1 * MAX_INT
        
        # A needs to be the smaller array - we run binary search to find position for a
        if len(A) > len(B):
            A, B = B, A
        total_len = len(A) + len(B)
        half_len = total_len // 2
        
        left, right = 0, len(A) - 1
        
        while True:
            # x_part is the index where you partition nums1
            i = (left + right) // 2            
            j = half_len - i - 2 # -2 to account for x_part and y_part starting at 0; logic for y_part is: 2(x_part + y_part) = len(x) + len(y)
            
            Aleft = A[i] if i >= 0 else MIN_INT
            Aright = A[i + 1] if (i + 1) < len(A) else MAX_INT
            
            Bleft = B[j] if j >= 0 else MIN_INT
            Bright = B[j + 1] if (j + 1) < len(B) else MAX_INT
            
            if Aleft <= Bright and Bleft <= Aright:
                # Right partition points found for x and y; median can be picked from these elements
                # If combined list has odd number of elements, right side will have one extra element
                if total_len % 2:
                    median = min(Aright, Bright)
                    return median
                else:
                    # If combined list has even number of elements
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                    return median
            elif Aleft > Bright: # partition point is too far on the right side of x, go to left side; too many elements from A in partition
                right = i - 1
            else:
                left = i + 1