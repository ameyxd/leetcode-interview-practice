class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map complement to current position
        complement_map = defaultdict()
        for i, num in enumerate(nums):
            if num in complement_map:
                return [complement_map[num], i]
            complement_map[target - num] = i
        