class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Keep shifting n to the right by i then and with 1 to get the bit
            # We shift by i because we are not updating and reducing n, so each time we want the next bit, we need to move all the bits right by i
            bit = (n >> i) & 1
            # We need to add bits to res in reverse order, so place bits starting with 31st position (start of res in binary form) and go forward
            # The way to add bits while preserving the previous bits is to take the or. Write this dows with an example and it will make sense.
            res = res | (bit << (31 - i))
        return res
