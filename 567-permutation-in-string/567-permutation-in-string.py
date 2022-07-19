class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            s2Map = Counter(s2[i: i + len(s1)])
            if s2Map == s1Map:
                return True
        return False