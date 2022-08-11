class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s, count_t = {}, {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            
        # count_s, count_t = Counter(s), Counter(t)
        
        for char, freq in count_t.items():
            if freq - count_s.get(char, 0) == 1:
                return char
        