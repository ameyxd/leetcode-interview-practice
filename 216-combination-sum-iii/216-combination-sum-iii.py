class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        combination = []
        
        def backtrack(start, remain):
            if len(combination) == k and remain == 0:
                res.append(combination.copy())
                return
            elif len(combination) == k or remain < 0:
                return
            # iterate through reduced list of candidates
            for i in range(start, 9):
                # if i not in combination:
                combination.append(i + 1)
                backtrack(i + 1, remain - i - 1)
                combination.pop()

        backtrack(0, n)
        return res