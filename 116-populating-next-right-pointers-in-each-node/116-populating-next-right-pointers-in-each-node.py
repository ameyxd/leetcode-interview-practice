"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # BFS level order
    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = collections.deque([root])
        
        while queue:
            prev = None
            for i in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node
        return root
    
    # Save space without using queue
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # traverse leftmost node and make use of next pointers to make links.
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            curr = leftmost
            while curr:
                # establish connection between two nodes with same parent
                if curr.left and curr.right:
                    curr.left.next = curr.right
                # establish connection between two nodes with different parents
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left
        return root