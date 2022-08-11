class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking since we need all possible combinations
        ans = []
        
        def backtrack(s = [], left = 0, right = 0):
            # Base case
            if len(s) == 2 * n:
                ans.append("".join(s))
                return
            
            # Placing (
            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()
            
            # Placing )
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()
        
        backtrack()
        return ans