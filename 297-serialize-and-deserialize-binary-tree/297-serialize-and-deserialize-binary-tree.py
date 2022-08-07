# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        flattened = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                flattened.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                flattened.append("N")
        return ','.join(flattened)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        flattened = data.split(',')
        root = TreeNode(int(flattened[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            # if node has children they will be at positions i and i + 1
            leftC, rightC = flattened[i], flattened[i + 1]
            if leftC != "N":
                left = TreeNode(int(leftC))
                node.left = left
                queue.append(left)
            if rightC != "N":
                right = TreeNode(int(rightC))
                node.right = right
                queue.append(right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))2