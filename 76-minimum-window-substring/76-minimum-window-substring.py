class Solution(object):
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # First find the valid substring, then reduce the length from the starting point

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

    # using better names
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "": return ""
        l = 0
        res, resLen = [-1, -1], float("infinity")
        countT, window = {}, {}        
        countT = Counter(t) # or for c in t: countT = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # does window[c] satisfy adding a character present in t? 
            if c in countT and window[c] == countT[c]:
                have += 1
            # Valid string found if
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # Shrink from left
                window[s[l]] -= 1
                # if we shrink and the char was present in t, have will decrease because you don't have that one char in updated substring
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1]# if resLen != float("infinity") else ""