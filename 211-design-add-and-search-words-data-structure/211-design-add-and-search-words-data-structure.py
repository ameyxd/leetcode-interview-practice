class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        
    def search(self, word: str) -> bool:
        
        def dfs(j, root):
        
            node = root

            for i in range(j, len(word)):
                char = word[i]

                if char == '.':
                    # Recursively go checking in DFS manner for match
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False                
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.end_of_word
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)