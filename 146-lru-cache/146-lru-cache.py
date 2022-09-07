class DoublyLinkedListNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None

# You need linked list to maintain the recent use order. Doubly linked makes it easier. To make the access to each node O(1) you use a hashmap called cache.
# To initialize, you need a linked list node class object
# Always have a dummy head node and tail node that are doubly linked and add nodes in the middle

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = {} # Map val to ref to LL node
        self.head, self.tail = DoublyLinkedListNode(), DoublyLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        # The node with that key becomes most recently used so it goes to the front of the LL
        node = self.cache.get(key, None)
        if not node:
            return -1
        # Remove node from its position
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # Place at front since it is now most recently used
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

        return node.value
        

    def put(self, key: int, value: int) -> None:
        # The node is inserted at the front, and if the size exceeds capacity, last node is removed
        
        node = self.cache.get(key)
        
        if node:
            node.value = value
            # Sent to front
            
            # remove from back
            node.prev.next = node.next
            node.next.prev = node.prev

            # send to front            
            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
        else:
            node = DoublyLinkedListNode()
            node.key = key
            node.value = value

            # Insert node
            self.cache[key] = node

            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node

            self.size += 1

            if self.size > self.cap:
                # Remove last node
                
                res = self.tail.prev
                res.prev.next = res.next
                res.next.prev = res.prev
                tail = res
                
                del self.cache[tail.key]
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)