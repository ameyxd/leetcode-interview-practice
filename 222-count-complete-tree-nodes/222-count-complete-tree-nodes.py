# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exists(self, index, root, d):
        node = root
        for i in range(d):
            bit = (d - 1) - i
            if (index >> bit) & 1:
                node = node.right
            else:
                node = node.left
        # node = root
        # left, right = 0, 2**d - 1
        # for _ in range(d):
        #     pivot = left + (right - left) // 2
        #     if index <= pivot:
        #         node = node.left
        #         right = pivot
        #     else:
        #         node = node.right
        #         left = pivot + 1
        if node:
            return True
        else:
            return False
        
    def getDepth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # # Doesn't take advantage of the fact that this is a complete binary tree
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
        if not root:
            return 0

        d = self.getDepth(root)

        if d == 0:
            return 1
        
        # last level nodes are from 0 to 2**d - 1
        left, right = 0, 2**d - 1
        while left <= right:
            middle = left + (right - left) // 2
            if self.exists(middle, root, d):
                left = middle + 1
            else:
                right = middle - 1
        
        return left + (2 ** d - 1)