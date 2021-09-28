class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signCount = 0
        if 0 in nums:
            return 0
        else:
            for n in nums:
                if n < 0:
                    signCount += 1
            return -1 if signCount % 2 else 1