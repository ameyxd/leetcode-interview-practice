class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # Using zip
        res = []
        
        for n1, n2 in zip([lower - 1] + nums, nums + [upper + 1]):
            if n2 - n1 == 2:
                # missing number is single number
                res.append(str(n1 + 1))
            elif n2 - n1 > 2:
                res.append(str(n1 + 1) + "->" + str(n2 - 1))
                
        return res
        
        
    def findMissingRanges1(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        def addrange(prev, curr):
            if prev > curr:
                return
            if prev == curr:
                res.append(str(prev))
            else:
                res.append(str(prev) + '->' + str(curr))
                
        if not nums:
            addrange(lower, upper)
            return res
        
        addrange(lower, nums[0] - 1)
        
        for i in range(1, len(nums)):
            curr, prev = nums[i], nums[i - 1]
            if curr - prev > 1: # there are missing numbers between curr and prev
                addrange(prev + 1, curr - 1)

        addrange(nums[-1] + 1, upper)

        return res 
        