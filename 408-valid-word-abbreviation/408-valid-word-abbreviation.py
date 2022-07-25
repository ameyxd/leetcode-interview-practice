class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j] == '0':
                return False
            if word[i] == ' ':
                i += 1
            elif abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            elif abbr[j].isdigit():
                num = ""
                while j < len(abbr) and abbr[j].isnumeric():
                    num += abbr[j]
                    j += 1
                i += int(num)
        return i == len(word) and j == len(abbr)