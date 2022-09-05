class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        i = 0
        while True:
            if n < i:
                return i - 1
            n -= i
            i += 1
        