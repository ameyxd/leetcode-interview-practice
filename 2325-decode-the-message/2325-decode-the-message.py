class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        keyMap = {" ": " "}
        i = 0
        
        for char in key:
            if char not in keyMap:
                # print(char)
                keyMap[char] = chr(i + ord("a"))
                print(char, chr(i + ord("a")))
                i += 1
        ans = []
        for char in message:
            ans.append(keyMap[char])
            
        return "".join(ans)