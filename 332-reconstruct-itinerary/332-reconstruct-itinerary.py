class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithms
        # O(E * log(E/V)) time and O(E + V) space
        
        # Postorder DFS - append nodes after all nodes have been visited and popped: 
        # https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
        adj = defaultdict(list)
        for p1, p2 in tickets:
            adj[p1].append(p2)
            
        for city in adj:
            adj[city].sort(reverse=True) # since stack will need to pop and we need lexical order 
        
        itinerary = []
        
        def dfs(node):
            while adj[node]:
                curr = adj[node].pop()
                dfs(curr)
            itinerary.append(node)
        
        dfs("JFK")
        return itinerary[::-1]
