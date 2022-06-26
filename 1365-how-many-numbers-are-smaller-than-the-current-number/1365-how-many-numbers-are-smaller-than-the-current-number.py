class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort and map positions O(nlogn)
        sorted_nums = sorted(nums)
        d = {sorted_nums[0]: 0}
        curr = sorted_nums[0]
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] > curr: 
                d[sorted_nums[i]] = i
            # Essentially, if the next sorted number is the same as the current sorted number, do nothing
            curr = sorted_nums[i]
        
        return [d[nums[i]] for i in range(len(nums))]

    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        # Brute force: O(n^2)
        output = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    counter += 1
            output.append(counter)
        return output
    
#         d = {}
#         for idx, num in enumerate(sorted(nums)):
#             d[num] = idx
        
#         res = []
#         for num in nums:
#             res.append(d[num])
        
#         return res
