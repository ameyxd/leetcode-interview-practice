class Solution:
    def countSubstrings(self, s: str) -> int:
        # Very similar to longest palindromic substring: Search for palindromes such that char at i is at center of palindrome
        # DP because subproblems: "abaaba" is made up of "baab" is made up of "aa"
        # Time: O(n^2)
        def countPalindromes(s, l, r):
            res = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
            

        res = 0
        for i in range(len(s)):
            # Odd length substrings
            l, r = i, i
            res += countPalindromes(s, l, r)
            # Even length substrings
            l, r = i, i + 1
            res += countPalindromes(s, l, r)

        return res