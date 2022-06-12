class Solution:
    def countBits1(self, n: int) -> List[int]:
        # Using bit counting for each element
        def hammingWeight(x):
            count = 0
            while x > 0:
                if x & 1:
                    count += 1
                x >>= 1
            return count
        
        return [hammingWeight(i) for i in range(n + 1)]
    
    # DP Solution using the least significant bit -> Ans(x) = Ans(x/2) + (x % 2) [which is the last significant digit]
    
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = ans[x >> 1] + (x & 1) # x >> 1 is x/2 and x&1 is the same as x%2 i.e. least significant bit
        return ans