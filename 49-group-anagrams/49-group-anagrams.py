class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Strategy: Map character counts for each string as a list TO the anagram strings using a dict
        res = defaultdict(list) # defautdict so we don't have to worry about keyerror key not present
        
        for s in strs:
            charCount = [0] * 26
            for char in s:
                charCount[ord(char) - ord("a")] += 1 # so a-z can be mapped to 0-26
            res[tuple(charCount)].append(s)
        return res.values()
