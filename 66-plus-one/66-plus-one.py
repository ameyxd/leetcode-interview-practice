class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + carry
            print(num)
            carry = num // 10
            num = num % 10
            res.append(num)
        if carry == 1:
            res.append(1)
        return res[::-1]