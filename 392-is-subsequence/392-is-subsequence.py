class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
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
        # return s.isSubset(t) or t.isSubset(s)
        # return set(s) <= set(t) or set(t) <= set(s)