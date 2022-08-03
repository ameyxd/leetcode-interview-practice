class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        nums.sort()
        
        i = 0
        while i < len(nums):
            first = nums[i]
            # start generating number groups            
            for j in range(k):
                nextNum = first + j
                if nextNum not in counter:
                    # the number cannot be used to generate the group of consecutive numbers
                    print(nextNum)
                    return False
                counter[nextNum] -= 1
                if counter[nextNum] == 0:
                    del counter[nextNum]
            while i < len(nums) and nums[i] not in counter:
                i += 1
        return True