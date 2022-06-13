class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True
        
    # for Time limit exceeded - add prune function: I still don't understand this
    def prune(self, word):
        curr = self
        stack = []
        
        for char in word:
            stack.append(curr)
            curr = curr.children[char]
        curr.end_of_word = False
        
        for t_node, ch in reversed(list(zip(stack, word))):
            if len(t_node.children[ch].children) > 0:
                return
            else:
                del t_node.children[ch]
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visit or 
                board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end_of_word:
                res.add(word)
                root.prune(word) # prune from trie when new word found
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
                        
            visit.remove((r, c)) # backtracking
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)