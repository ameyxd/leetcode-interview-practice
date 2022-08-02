class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []
        
        def backtrack(start):
            if start >= len(s):
                res.append(pal[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if substring == substring[::-1]: # Palindrome
                    pal.append(substring)
                    backtrack(end + 1)
                    pal.pop()
        backtrack(0)
        return res