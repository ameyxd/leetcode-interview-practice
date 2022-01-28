class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Two pointer solution:
        
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                delete_i = s[i + 1: j + 1]
                delete_j = s[i: j]
                return delete_i == delete_i[::-1] or delete_j == delete_j[::-1]
        return True