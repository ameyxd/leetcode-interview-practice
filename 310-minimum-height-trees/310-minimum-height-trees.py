class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Strat: Topological sort will help because leaf nodes, i.e., nodes that have no 'outgoing edges' (this is an undirected graph so no outgoing edges means 1 edge min, not 0) 
        # nodes that have 1 outgoing edge (leaves) cannot be the root of the minimum height tree since a tree rooted on any adjacent non-leaf node will always have a shorter height
        
        # At most two potential candidates for root of MHTs will remain, since we will remove edges, i.e., decrease indegree of nodes adjacent to leaves one by one
        # Leaves will be maintained in the same queue like in source queues, i.e., at any point, the queue will have only leaves
        # Since we need to remove edges/reduce indegree for all nodes linked to a leaf at once, we will run a for loop on len of queue

        # Build adj list and indegree hashmap
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
            # Since we need to remove edges/reduce indegree for all nodes linked to a leaf at once, we will run a for loop on len of queue
            for i in range(numLeaves):
                node = leaves_q.popleft()
                for child in adj[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        leaves_q.append(child)
        # In the end, the queue will only contain nodes that will have the minimum height trees if picked as root nodes
        return list(leaves_q)