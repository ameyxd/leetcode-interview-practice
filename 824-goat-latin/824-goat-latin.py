class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        wordlist = sentence.split(' ')
        for i, word in enumerate(wordlist):
            newword = ""
            # starts with vowel
            if word[0].lower() in vowels:
                newword = word + "ma"
            else: # starts with consonant
                newword = word[1:] + word[0] + "ma"
            # add 'a'
            newword += "a" * (i + 1)
            res.append(newword) # add to res
        return " ".join(res)