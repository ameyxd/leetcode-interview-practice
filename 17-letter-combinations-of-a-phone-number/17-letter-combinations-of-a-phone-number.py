class Solution:
    # Backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letterMap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res = []
        s = []
        def backtrack(start):
            if len(s) == len(digits):
                res.append("".join(s))
                return
            poss_letters = letterMap[int(digits[start])]
            for letter in poss_letters:
                s.append(letter)
                backtrack(start + 1)
                s.pop()
        backtrack(0)
        
        return res
    