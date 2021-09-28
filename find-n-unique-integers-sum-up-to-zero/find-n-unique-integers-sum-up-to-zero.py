class Solution:
    def sumZero(self, n: int) -> List[int]:
        d, rem = n//2, n%2
        return [e for e in list(range(-d, d+1))] if rem else [e for e in list(range(-d, d+1)) if e]
        
        # if not n % 2:
        #     return (list(range(-n//2+1, n//2+1)).remove(0))
        # else:
        #     return (list(range(-n//2+1, n//2+1)))
