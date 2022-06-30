class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_str = ''.join([char for char in s.lower() if char.isalnum()])
        # re.sub('^[a-zA-Z0-9]', '', s).lower() # Regex solution

        return raw_str == raw_str[::-1]
