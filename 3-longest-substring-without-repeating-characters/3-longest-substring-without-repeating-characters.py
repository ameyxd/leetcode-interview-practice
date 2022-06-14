class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charmap = {}
        begin, end, max_len = 0, 0, 0
        for end in range(len(s)):
            curr = s[end]
            if curr in charmap:
                begin = max(begin, charmap[curr] + 1)
            charmap[curr] = end
            max_len = max(max_len, end - begin + 1)
        return max_len
    
    
    """Note: Use example 'abba' to explain line 12"""
    
    '''
    
    Strat:
    
    Sliding window logic: have begin and end indexes, move end index one by one and add each char to a dict mapping char->last seen index of that char. This way, when you encounter a char in dict, you move the begin index to max of begin and (the duplicate char loc + 1). Keep updating the dict and the max_len.
    
    Another way to remember: The most important part is what you do when you encounter a repeating character, i.e., character present in the hashmap. You update the start of the string to the index of the duplicate character to ensure no repeating characters in substring formed after. If the current duplicate found occurred before the start, that means that character is new to the substring.
    
    Another way to understand:
    
    Need 3 temporary variables to find the longest substring: start, maxLength, and usedChars.
    Start by walking through string of characters, one at a time.
    Check if the current character is in the usedChars map, this would mean we have already seen it and have stored it's corresponding index.
    If it's in there and the start index is <= that index, update start to the last seen duplicate's index+1. This will put the start index at just past the current value's last seen duplicate. This allows us to have the longest possible substring that does not contain duplicates.
    If it's not in the usedChars map, we can calculate the longest substring seen so far. Just take the current index minus the start index. If that value is longer than maxLength, set maxLength to it.
    Finally, update the usedChars map to contain the current value that we just finished processing.
    
    ''' 
    