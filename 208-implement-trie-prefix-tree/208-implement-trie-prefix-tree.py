class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = None
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_of_word = True
        

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)