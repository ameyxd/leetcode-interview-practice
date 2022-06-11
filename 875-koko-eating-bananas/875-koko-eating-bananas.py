import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Same strat as 1011. (Capacity to ship packages) and 410. (Split array largest sum)
        # Brute force could be look through all values of k - time complexity = O(max(p) * p)
        # Use binary search over search space k
        
        def feasible(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            return total <= h # Means piles can be eaten with speed speed within h hours
        
        left, right = 1, max(piles) # Banana eating speed can be min 1 and max the size of the largest pile
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left