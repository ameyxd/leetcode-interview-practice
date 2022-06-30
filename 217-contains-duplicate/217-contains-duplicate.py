class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = collections.Counter(nums)
        # return not all(count == 1 for count in count_dict.values())
        for count in list(count_dict.values()):
            if count > 1:
                return True
        return False