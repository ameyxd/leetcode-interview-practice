# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        treelist = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                treelist.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                treelist.append("*")
        return ",".join(treelist)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        tree = deque(data.split(","))
        root = TreeNode(tree.popleft())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left = tree.popleft()
            right = tree.popleft()
            if left != "*":
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right != "*":
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root
                
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans