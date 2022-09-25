class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict() # Can also use Counter
        for char in s:
            # can also use Counter
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        # Check one by one from the string s and return the position of the first char that has 1 count in the Counter
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1