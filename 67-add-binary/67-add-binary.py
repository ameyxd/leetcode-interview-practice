class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = []
        n = max(len(a), len(b))
        i, j = len(a) - 1, len(b) - 1
        if i < 0:
            return b
        if j < 0:
            return a
        
        # Add leading 0s and reverse strings, then add them together
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        a, b = a[::-1], b[::-1]
        ans = []
        carry = 0
        for i in range(n):
            dig_tot = carry + int(a[i]) + int(b[i])
            carry = dig_tot // 2
            dig_tot = dig_tot % 2
            if dig_tot:
                ans.append('1')
            else:
                ans.append('0')
        if carry:
            ans.append('1')
            
        return "".join(ans[::-1])
        
