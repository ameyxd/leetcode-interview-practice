class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []
        
        def backtrack(start, remain):
            if remain == 0:
                res.append(combination.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if remain > 0:
                    combination.append(candidates[i])
                    backtrack(i + 1, remain - candidates[i])
                    combination.pop()
            
        backtrack(0, target)
        return res