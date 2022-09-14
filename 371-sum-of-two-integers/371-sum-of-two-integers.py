class Solution:
    def getSum(self, a: int, b: int) -> int:
        sum_wo_carry, carry = abs(a), abs(b)
        if b > a:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # Sum of two numbers
            while carry != 0:
                sum_wo_carry, carry = sum_wo_carry ^ carry, (sum_wo_carry & carry) << 1
        else:
            # difference of two numbers
            while carry != 0:
                sum_wo_carry, carry = sum_wo_carry ^ carry, (~sum_wo_carry & carry) << 1
                
        return sum_wo_carry * sign