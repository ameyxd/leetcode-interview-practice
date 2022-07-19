class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = None

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
        
    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return node.end
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)

            return False
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)