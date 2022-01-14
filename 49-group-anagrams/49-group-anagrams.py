class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Strategy: Map character counts as a list to the anagram strings using a dict
        res = defaultdict(list)
        
        for s in strs:
            charCount = [0] * 26
            for char in s:
                charCount[ord(char) - ord("a")] += 1 # so a-z can be mapped to 0-26
            res[tuple(charCount)].append(s)
        return res.values()
