import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
#         edited_str = ''.join(char for char in s.lower() if char.isalnum())
#         return edited_str == edited_str[::-1]
    
        # Regex solution
        edited_str = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return edited_str == edited_str[::-1]