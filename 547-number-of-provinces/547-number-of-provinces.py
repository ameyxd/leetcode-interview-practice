class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for child in range(len(isConnected)):
                if child not in visited and isConnected[node][child] == 1:
                    dfs(child)
            
        
        visited = set()
        count = 0        
            
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1
        return count
        