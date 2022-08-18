class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Strat is whenever you encounter two # that means the leaf has been reached, so replace that with a # (basically collapse that leaf)
        stack = []
        
        for node in preorder.split(","):
            stack.append(node)
            while len(stack) > 1 and stack[-1] == stack[-2] == "#":
                # Pop the leaves
                stack.pop()
                stack.pop()
                if not stack: # Invalid preorder
                    return False
                # Collapse current node to leaf
                stack[-1] = "#"
        return stack == ["#"] # Last value, i.e., collapsed node is the valid root