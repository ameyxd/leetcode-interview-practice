class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Use topological sort
        
        indegree = {}
        for word in words:
            for char in word:
                indegree[char] = 0
        
        adj = collections.defaultdict(list)
        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            for j in range(0, min_len):
                parent, child = w1[j], w2[j]
                if parent != child:
                    adj[parent].append(child)
                    indegree[child] = indegree.get(child, 0) + 1
                    break
                elif j == min_len - 1 and len(w1) > len(w2):
                    return ""
                
        queue = collections.deque([k for k in indegree.keys() if indegree[k] == 0])
        top_sort_order = []
        
        while queue:
            word = queue.popleft()
            top_sort_order.append(word)
            for child in adj[word]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        if len(top_sort_order) != len(indegree):
            return ""
        
        print(top_sort_order)
        
        return ''.join(top_sort_order) #if len(top_sort_order) == len(indegree) else ""