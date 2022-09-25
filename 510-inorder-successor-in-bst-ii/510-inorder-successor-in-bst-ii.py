"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # if node has right child, successor to the node is the left most node in the right subtree
        # if node does not have a right child, successor to the node is the nearest ancestor which is the left child
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            while node.parent and node.parent.right == node: # can also just check the first node that has a value greater than the node we are checking for
                node = node.parent
            return node.parent