class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Always start with prefix sums: instead of looking at the sum of a range, we only look at two different values
        # (P[r] - P[l - 1]) % k = 0
        # P[r] % k == P[l - 1] % k
        
        prefixSum = [0] * len(nums)
        runningSum = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            prefixSum[i] = runningSum
        print(prefixSum)
        
        # Maintain a hash set of remainder to index
        remMap = {}
        for i in range(len(nums)):
            rem = prefixSum[i] % k
            if rem not in remMap:
                remMap[rem] = i
            if rem in remMap and i - remMap[rem] > 1: # if you come across a prefixSum that has the same remainder as another prefixSum, that means the diff btw the prefixSums, i.e., the range of values sum is divisible by k
                # Second condition is to check length at least two
                return True
            if rem == 0 and i >= 1:
                # Subarray from start of len greater than or equal to 2
                return True
        return False