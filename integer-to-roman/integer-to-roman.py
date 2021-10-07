class Solution:
    def intToRoman(self, num: int) -> str:
        val_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = ""
        for val, sym in val_map:
            if val > num:
                continue
            mult = num // val
            for i in range(mult):
                res += sym
            num -= mult * val
        return res