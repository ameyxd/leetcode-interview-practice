class Solution:
    def mySqrt1(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            mult = mid * mid
            if mult == x:
                return mid
            elif mult > x:
                right = mid - 1
            else:
                left = mid + 1
        return right # Return right because the loop broke when left became greater than right and we are rounding off to the smallest integer (problem asks for floor)

        # Easier way with the basic template:
        # If we find the minimum k that satisfies k*k > x, then k - 1 is the answer since we are rounding to floor. Try with example of 8. Answer is 3 - 1 = 2, because 3 is the minimum k such that 3*3 > 8 

    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1 # x + 1 to handle x = 0, x = 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1 #Read comment above - we need to return floor