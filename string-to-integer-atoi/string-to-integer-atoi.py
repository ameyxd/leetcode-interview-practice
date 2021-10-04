class Solution:
    def myAtoi(self, s: str) -> int:
        strp = s.strip()
        MAX_INT, MIN_INT = 2**31-1, -2**31
        strp = re.search(r'^[-+]?\d+', strp)
        if not strp: return 0
        num = int(strp.group())
        # print(num)
        return min(max(num, MIN_INT), MAX_INT)
    
