class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(mlogm + nlogn) Time complexity
        nums1.sort()
        nums2.sort()
        dups = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                dups.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return dups
        

    # O(mlogn + nlogn) time if n is much larger than m
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
                
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums2.sort()
        
        def binarySearch(target):
            l, r = 0, len(nums2) - 1
            while l < r:
                mid = l + (r - l) // 2
                if nums2[mid] == target:
                    return True
                elif nums2[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return False
        
        dups = []
        for i in range(len(nums1)):
            if binarySearch(nums1[i]):
                dups.append(nums1[i])
        
        return dups