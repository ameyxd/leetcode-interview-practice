class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Strat: two visit sets - one to track all possible nodes accessible from pacific and one from atlantic
        # Recursive dfs - run dfs for leftmost and topmost elements to check accessibility from pacific and
        # rightmost and bottommost elements to check accesssibility from atlantic
        # Get intersection of the two sets
        
        rows, cols = len(heights), len(heights[0])
        visit_pac, visit_atl = set(), set()
        
        
        def dfs(row, col, visit_set, prev_h):
            if (row < 0 or col < 0 or row == rows or col == cols # invalid point 
                or prev_h > heights[row][col] # invalid point -> can't reach ocean from this point
                or (row, col) in visit_set): #already visited point
                    return
            # If we get to this point, that means this point is possible to visit from one of the oceans as per the visit_set sent in the function
            visit_set.add((row, col))
            dfs(row - 1, col, visit_set, heights[row][col])
            dfs(row + 1, col, visit_set, heights[row][col])
            dfs(row, col - 1, visit_set, heights[row][col])
            dfs(row, col + 1, visit_set, heights[row][col])
        
        
        # Fix the first and last row and check if they are accessible from pacific ocean and atlantic ocean respectively
        for col in range(cols):
            dfs(0, col, visit_pac, heights[0][col])
            dfs(rows - 1, col, visit_atl, heights[rows - 1][col])
        
        # Fix the first and last column and check if they are accessible from pacific ocean and atlantic ocean respectively
        for row in range(rows):
            dfs(row, 0, visit_pac, heights[row][0])
            dfs(row, cols - 1, visit_atl, heights[row][cols - 1])
        
        return (list(list(tuple) for tuple in visit_pac.intersection(visit_atl)))