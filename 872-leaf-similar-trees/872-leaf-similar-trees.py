# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSeq(root):
            stack = []
            curr = root
            seq = []
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                if not curr.left and not curr.right:
                    seq.append(curr.val)
                curr = curr.right
            return seq
        seq1, seq2 = getLeafSeq(root1), getLeafSeq(root2)
        print(seq1, seq2)
        return seq1 == seq2