class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for sec in path.split("/"):
            if sec == "..":
                if stack:
                    stack.pop()
            elif sec and sec != ".":
                stack.append(sec)
        return "/" + "/".join(stack)