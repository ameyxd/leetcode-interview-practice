class Solution:
    # Similar to 1249
    def minAddToMakeValid(self, s: str) -> int:
        # Strat is to count how many unmatched open and close parenthesis there are
        missing, left = 0, 0
        for par in s:
            if par == "(":
                left += 1
            else: 
                # There is a match to the )
                if left:
                    left -= 1
                else: # There is no match to the )
                    missing += 1
        return missing + left
        

    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s = s.replace("()", "")
        
        return len(s)