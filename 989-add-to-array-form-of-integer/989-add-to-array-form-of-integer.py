class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = "".join(str(i) for i in num)
        add = int(s) + k
        addstr = str(add)
        print(addstr)
        res = []
        for j in addstr:
            res.append(j)
        return res
        # res = 0
        # carry = 0
        # for i in range(len(num) - 1, -1, -1):
        #     n = num[i] + k % 10 + carry
        #     carry = n // 10
        #     n = n % 10
        #     k = k // 10
        #     res += n
        # # if carry == 1:
        # #     res += 1 * 10 ** (len(str(res)))
        # if k:
        #     print(k)
        #     while k:
        #         res+= k % 10
        #         k = k // 10
        # return res