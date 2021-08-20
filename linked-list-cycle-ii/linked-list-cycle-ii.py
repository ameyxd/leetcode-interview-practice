# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getLength(self, slow):
        curr = slow
        cycle_length = 0
        while True:
            curr = curr.next
            cycle_length += 1
            if curr == slow:
                break
        return cycle_length
    
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                cycle_length = self.getLength(slow)
                print(cycle_length)
                break
        else:
            return None
        return self.findStart(head, cycle_length)
        
    def findStart(self, head, cycle_length):
        ptr1, ptr2 = head, head
        while cycle_length:
            ptr2 = ptr2.next
            cycle_length -= 1
        while ptr1 != ptr2:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        return ptr1
            