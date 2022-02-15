class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Use topological sort
        
        # Initialize indegree dict
        indegree = {}
        for word in words:
            for char in word:
                indegree[char] = 0
        
        adj = collections.defaultdict(list)
        
        # Build adjacenecy list (graph) and indegree map
        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            for j in range(0, min_len):
                parent, child = w1[j], w2[j]
                if parent != child:
                    adj[parent].append(child)
                    indegree[child] = indegree.get(child, 0) + 1
                    break # Only the fist uncommon char matters when comparing two words
                elif j == min_len - 1 and len(w1) > len(w2): # "abc", "ab" gives an error, but "ab", "abc" doesn't -> fix using else statement
                    return ""
                
        source_queue = collections.deque([k for k in indegree.keys() if indegree[k] == 0])
        alien_dict = []
        
        # Run topological sort using a queue to keep track of all the sources (indegree == 0)
        while source_queue:
            word = source_queue.popleft()
            alien_dict.append(word) # Every letter out of the queue is one that has no remaining dependencies
            for child in adj[word]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    source_queue.append(child)
        
        
        return ''.join(alien_dict) if len(alien_dict) == len(indegree) else "" # if alien dict is not the same size as the number of characters we have in the list, there is a cycle, i.e., inconsistency in input so dict cannot be built