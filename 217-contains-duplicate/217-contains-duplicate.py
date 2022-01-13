class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        import collections
        c = collections.Counter(nums)
        if any(y > 1 for y in c.values()):
            return True
        else:
            return False