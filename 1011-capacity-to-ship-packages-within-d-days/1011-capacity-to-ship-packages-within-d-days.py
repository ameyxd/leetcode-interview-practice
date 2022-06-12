class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Binary search over capacity space, using the actual weights in the condition function
        
        # Target condition function
        def feasible(capacity):
            days_curr = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity: # need to send next day
                    total = weight # reset weight to next weight that needs to be loaded
                    days_curr += 1
                    if days_curr > days: # it takes more days that we are asked if we use the capacity provided to this function  
                        return False
            return True
            
        left, right = max(weights), sum(weights) # search space ranges from min capacity = max of any one weight, to max capacity = sum of all weights
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    # Given a capacity (that we iterate over), feasible function checks if number of days taken is more than given days.