class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Same as 1011: Use binary search in search space amongst possible m values and 875 (Koko eating bananas)
        # Harder to understand logic and why it works - review more
        
        def feasible(threshold):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        