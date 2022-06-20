class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Recursive solution O(t)
        if not s:
            return True
        if not t:
            return False
        
        # if there is a match
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
        return False

    
    # Two pointers solution O(t)
    def isSubsequence1(self, s: str, t: str) -> bool:
        left, right = 0, 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1
        return left == len(s)
