class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        # Two sum with two pointers after fixing the first two numbers, o(n^3)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Two sum by using two pointers
                l, r = j + 1, len(nums) - 1
                remaining = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remaining:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > remaining:
                        r -= 1
                    else:
                        l += 1
        return ans