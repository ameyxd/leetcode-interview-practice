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
            curr = carry
            if a[i] == '1':
                curr += 1
            if b[i] == '1':
                curr += 1
            rem = curr % 2
            carry = curr // 2
            
            if rem:
                ans.append('1')
            else:
                ans.append('0')
        if carry:
            ans.append('1')

        return "".join(ans[::-1])
        
