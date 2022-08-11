class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return target
                
        return ans