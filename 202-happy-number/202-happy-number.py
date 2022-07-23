class Solution:
    def isHappy(self, n: int) -> bool:
        setN = set()
        def nextSq(n):
            sumN = 0
            while n:
                sumN += (n % 10) ** 2
                n = n // 10
            return sumN
        while True:
            setN.add(n)
            n = nextSq(n)
            if n == 1:
                return True
            if n in setN:
                return False
            