class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         [1, 3, 4, 2, 2]
#         ITERATE THROUGH THE list and for every number that i see, i set that i to -i that corresponding element
#         if at any point, the number that is to be marked is already marked return that i
#         [1, 3*, 4*, 2*, 2*] => range of these numbers is 1....n
        
#         [6, 5, 2*, 3*, 5, 1*, 4*]
        
        for i, num in enumerate(nums):
            cur = abs(num)
            if nums[cur] < 0:
                break
            nums[cur] *= -1
            
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return cur