class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Levelwise BFS: it matters how you build the adj list
        if endWord not in wordList:
            return 0
        # Adj list stores a pattern mapped to the words that match that pattern O(nm^2)
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pos in range(len(word)):
                pattern = word[:pos] + "*" + word[pos + 1:] 
                adj[pattern].append(word)
                
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for pos in range(len(word)):
                    pattern = word[:pos] + "*" + word[pos + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            res += 1            
        return 0