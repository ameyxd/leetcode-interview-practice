class Solution:
    def findTheDifference1(self, s: str, t: str) -> str:
        count_s, count_t = {}, {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            
        # count_s, count_t = Counter(s), Counter(t)
        
        for char, freq in count_t.items():
            if freq - count_s.get(char, 0) == 1:
                return char

    # O(1) space complexity
    def findTheDifference(self, s: str, t: str) -> str:
        char = 0
        # XOR all chars in s
        for c in s:
            char ^= ord(c)
        
        # XOR all chars in t
        for c in t:
            char ^= ord(c)
        
        return chr(char)