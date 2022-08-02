class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        # Choose a num or don't for a subset, so 2^n subsets. Each subset could be up to length n, so Time Complexity = O(n * 2^n)
        # Try building the tree for backtracking
        res = []        
        subset = []
        #i is the index of the value we are passing
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            
            dfs(i + 1)
            
            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res
    
    # Backtracking traditional format
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Choose a num or don't for a subset, so 2^n subsets. Each subset could be up to length n, so Time Complexity = O(n * 2^n)
        # Try building the tree for backtracking
        res = []    
        subset = []
        
        def backtrack(start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        
        return res