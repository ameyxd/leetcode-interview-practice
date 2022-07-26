"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        visited = {} # Map old nodes to new nodes to ensure you're not creating multiple copies of the same node
        curr = head
        newNode = Node(curr.val, None, None)
        visited[curr] = newNode
        
        def getClonedNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
        
        while curr: # Iterate over linked list
            newNode.random = getClonedNode(curr.random) 
            newNode.next = getClonedNode(curr.next)
            
            curr = curr.next
            newNode = newNode.next
            
        return visited[head]