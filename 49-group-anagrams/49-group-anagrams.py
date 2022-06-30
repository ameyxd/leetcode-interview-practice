class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict mapping counts as list to anagram list
        # key: ([26 ints]) -> value: [list of anagrams]
        groupDict = {}
        for word in strs:
            key = [0] * 26
            for char in word:
                pos = ord(char) - ord('a')
                key[pos] += 1
            if tuple(key) in groupDict: # This if-else block can be removed by using defaultdict
                groupDict[tuple(key)].append(word)
            else:
                groupDict[tuple(key)] = [word]
        return groupDict.values()
        
        