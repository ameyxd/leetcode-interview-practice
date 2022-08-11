class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        first, last = -1, -1
        # can just use bisect left and bisect right functions in python
        
        # Find first occurence of the element
        def searchFirst():
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid # Always decrement right pointer to the point where l and r are equal
            if (l < len(nums) and nums[l] == target):
                return l
            else:
                return -1

        def searchLast():
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            if nums[r - 1] == target:
                return r - 1
            else:
                return -1

        first, last = searchFirst(), searchLast()
        print(first, last)
        
        return [first, last]
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        first, last = -1, -1
        # can just use bisect left and bisect right functions in python
        l, r = bisect_left(nums, target), bisect_right(nums, target)
        if l < len(nums) and nums[l] == target: first = l
        if nums[r - 1] == target: last = r - 1
        return [first, last]