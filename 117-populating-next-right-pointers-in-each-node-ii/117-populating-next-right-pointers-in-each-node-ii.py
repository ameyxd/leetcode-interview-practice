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
    def connect1(self, root: 'Node') -> 'Node':
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

    # No extra space using pointers
    def connect(self, root: 'Node') -> 'Node':
        tail = dummy = Node(0)        
        node = root
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next                
        return root