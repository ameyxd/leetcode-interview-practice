class Solution:
    # DP Solution
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = True
                    break
        return dp[0]
    
    # BFS with queue
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = collections.deque([s])
        seen = set()
        while q:
            currS = q.popleft()
            for word in wordDict:
                if currS.startswith(word):
                    newS = currS[len(word):]
                    if newS == "":
                        return True
                    if newS not in seen:
                        q.append(newS)
                        seen.add(newS)
                        
        return False