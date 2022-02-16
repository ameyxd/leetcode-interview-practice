class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n:
            return []
        if n == 1:
            return [0]
        
        # Initialize graph
        indegree = {i: 0 for i in range(n)}
        adj = {i: [] for i in range(n)}
        
        # Build graph
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adj[n1].append(n2)
            adj[n2].append(n1)
            indegree[n1] += 1
            indegree[n2] += 1
        
        
        leaves_q = collections.deque([k for k in indegree.keys() if indegree[k] == 1]) # Leaves queue is only made of elements that have no indegree, i.e., are leaf nodes
        # print(indegree, leaves_q)
        
        totalNodesLeft = n
        
        # Remove leaves level by level: which means for loop will run for all elements in the queue
        while totalNodesLeft > 2:
            numLeaves = len(leaves_q)
            totalNodesLeft -= numLeaves
            for i in range(numLeaves):
                node = leaves_q.popleft()
                for child in adj[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        leaves_q.append(child)

        return list(leaves_q)