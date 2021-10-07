class Solution:
    def myAtoi(self, s: str) -> int:
        strp = s.strip()
        strp = re.match(r'^[-+]?\d+', strp)
        INTMAX, INTMIN = 2**31-1, -2**31
        if not strp: return 0
        num = int(strp.group())
        return min(INTMAX, max(INTMIN, num))