class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        maxLen = 0
        charMap = {} # Map char to last seen index of char -> updated every time new char is seen

        for end in range(len(s)):
            curr = s[end]
            
            if curr in charMap:
                start = max(start, charMap[curr] + 1) # not set to end + 1 because there may be occurrences of same char before end so charMap[curr] + 1
                
            charMap[curr] = end
            maxLen = max(maxLen, end - start + 1)
        return maxLen