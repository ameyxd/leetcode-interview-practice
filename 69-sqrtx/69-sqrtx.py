class Solution:
    def mySqrt(self, x: int) -> int:
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