class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = {}
        for i, val in enumerate(order):
            ordermap[val] = i
            
        # Compare every two words
        for i in range(len(words) - 1):
            currword = words[i]
            nextword = words[i + 1]
            
            # Compare the chars at each position
            for j in range(len(currword)):
                # If word that comes first is longer and the chars are the same so far return false
                if j >= len(nextword):
                    return False
                
                # if chars don't match, check ordermap
                if currword[j] != nextword[j]:
                    # If not in order from ordermap return False
                    if ordermap[currword[j]] > ordermap[nextword[j]]:
                        return False
                    # No need to check remaining letters
                    break
                    
        return True