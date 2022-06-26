class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        # char_count = {}
        # for char in s:
        #     char_count[char] = char_count.get(char, 0) + 1
        
        final_count = 0
        odd_chars = False
        for char in char_count:
            # Even number of chars, add to final count
            if char_count[char] % 2 == 0:
                final_count += char_count[char]
            else:
                # If number of occurrences of odd characters is a larger odd number n, it can still be used n - 1 times
                final_count += char_count[char] - 1
                odd_chars = True
        
        # If a single odd character is present, add 1 since it can go in the middle

        if odd_chars:
            final_count += 1
        
        return final_count