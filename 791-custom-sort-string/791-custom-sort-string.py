class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []
        
        for char in order:
            # Go in order
            if char in s:
                res.append(char * counter[char])
                counter[char] = 0
        
        # Remaining characters in counter that are not present in the order so they can be added at the end in any order
        for c in counter:
            res.append(c * counter[c])
            
        return "".join(res)