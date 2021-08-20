class Solution:
        
    def digitSquareSum(self, n):
        sq_sum  = 0
        while n:
            dig = n % 10
            sq_sum += dig * dig
            n //= 10
        return sq_sum
    
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(self.digitSquareSum(fast))
            if slow == fast:
                break
        return slow == 1
        
