class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = 0
        from collections import Counter
        t_dict = Counter(t)
        # t_dict = {}
        t_count = len(t_dict) # need t_count because it helps keep track of how many chars from t are missing in substring
        min_substring = ""
        
        
        for end in range(len(s)):
            # Find a substring that contains all chars of t
            curr = s[end]
            if curr in t_dict:
                t_dict[curr] -= 1
                if t_dict[curr] == 0:
                    t_count -= 1

            # When t_count is 0, that means valid substring is found. Now try to reduce its size
            while t_count == 0:
                window = end - start + 1
                if not min_substring or window < len(min_substring): # update min_substring
                    min_substring = s[start: end + 1]
                left_char = s[start]
                if left_char in t_dict: # add char back to t_dict and increment t_count
                    t_dict[left_char] += 1
                    if t_dict[left_char] > 0:
                        t_count += 1
                start += 1
        return min_substring
        
"""First find the valid substring, then reduce the length from the starting point"""