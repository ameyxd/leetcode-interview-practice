class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # The main concern the problem is trying to address is the duplicates
        # Logic: tree where you make two decisions - either select or not select a candidate
        
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy()) # we will use curr again below so append a copy
                return
            if i >= len(candidates) or total > target:
                return
            
            # include value at i
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            cur.pop()
            # or not include value at i
            dfs(i + 1, cur, total)
            
        
        dfs(0, [], 0)
        return res