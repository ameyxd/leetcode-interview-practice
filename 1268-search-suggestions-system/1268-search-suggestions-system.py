class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = None
        self.words = []
        
class Solution:
    # Modify the Trie data structure to keep track of words for every node
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.words.append(word)
            curr.words.sort()
            while len(curr.words) > 3:
                curr.words.pop()
        curr.end = True
    
    
    def getSuggestions(self, word):
        res = []
        curr =self.root
        for char in word:
            if char not in curr.children:
                break
            curr = curr.children[char]
            res.append(curr.words)
        return res        
    
    
    def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
        for product in products:
            self.insert(product)
        
        return self.getSuggestions(searchWord)
    
    # Two pointers approach
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        l, r = 0, len(products) - 1
        res = []
        products.sort()
        
        for i in range(len(searchWord)):
            c = searchWord[i]
            
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            
            res.append([])
            remain = r - l + 1
            for j in range(min(remain, 3)):
                res[-1].append(products[l + j])
        return res