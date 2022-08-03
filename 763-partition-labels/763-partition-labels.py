class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # one partitioned string has to be until the last occurrence of a starting character
        charMap = {k: v for v, k in enumerate(s)} # maps every unique character to the index of the last occurrence of that character
        for i, char in enumerate(s):
            charMap[char] = max(charMap[char], i)
        res = []
        end, currLen = 0, 0
        for i, c in enumerate(s):
            currLen += 1        
            end = max(end, charMap[c])
            if i == end:
                res.append(currLen)
                currLen = 0
        return res