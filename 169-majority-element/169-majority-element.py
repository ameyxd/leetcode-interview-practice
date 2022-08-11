class Solution:
    # Boyer Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidates = None
        
        for num in nums:
            if count == 0:
                candidate = num # reset search space by discarding previous instances of majority elements
            count += (1 if num == candidate else -1)
        
        return candidate