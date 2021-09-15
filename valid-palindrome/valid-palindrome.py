class Solution:
    def isPalindrome(self, s: str) -> bool:
        edited_str = ''.join(char for char in s.lower() if char.isalnum())
        return edited_str == edited_str[::-1]