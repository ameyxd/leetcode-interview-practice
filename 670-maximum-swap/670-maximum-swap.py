class Solution:
    def maximumSwap(self, num: int) -> int:
        # Prestoring indices in hashmap, if you find a bigger digit, swap
        # Greedy
        nstr = list(str(num))
        # Record last seen index
        intMap = {}
        for idx, dig in enumerate(nstr):
            intMap[dig] = idx
        
        for i, char in enumerate(nstr):
            # Check if a larger digit than current digit exists later in the number
            for d in range(9, int(char), -1): # Check in reverse
                digit = str(d)
                if digit in intMap and intMap[digit] > i:
                    # Swap
                    nstr[i], nstr[intMap[digit]] = nstr[intMap[digit]], nstr[i]
                    return ("".join(nstr))
        return num
        
    def maximumSwap_bruteforce(self, num: int) -> int:
        # Brute force is swap all possible pairs and maintain maximum O((len(num)^2)), space = O(n)
        maxn = num
        nstr = list(str(num))
        for i in range(len(nstr)):
            for j in range(i + 1, len(nstr)):
                tmp = nstr[i]
                nstr[i] = nstr[j]
                nstr[j] = tmp
                maxn = max(int("".join(nstr)), maxn)
        return maxn