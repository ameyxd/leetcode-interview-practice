class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window - slide l and r anytime substring becomes invalid, i.e., no of possible replacements in the string > k
        
        l = 0
        count = {}
        res = 0 # length of longest window
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            substringLen = r - l + 1
            mostFreqCount = max(count.values())
            
            # shift l to the right if invalid substring
            if substringLen - mostFreqCount > k: # understand why this is correct - this condition is the starting point for code and intuition 
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)   # can't use substringLen here because we just incremented l
                
        return res
    
    # O(26*n)