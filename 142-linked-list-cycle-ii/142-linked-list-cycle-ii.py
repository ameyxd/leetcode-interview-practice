# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getLength(self, slow):
        curr = slow
        len_cycle = 0
        while True:
            curr = curr.next
            len_cycle += 1
            if curr == slow:
                break
        return len_cycle
    
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                len_cycle = self.getLength(slow)
                break
        else:
            return None
        
        return self.findStart(head, len_cycle)
    
    
    def findStart(self, head, len_cycle):
        ptr1, ptr2 = head, head
        while len_cycle:
            ptr1 = ptr1.next
            len_cycle -= 1
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1

    
#     def getLength(self, slow):
#         curr = slow
#         cycle_length = 0
#         while True:
#             curr = curr.next
#             cycle_length += 1
#             if curr == slow:
#                 break
#         return cycle_length
    
#     def detectCycle(self, head: ListNode) -> ListNode:
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
            
#             if fast == slow:
#                 cycle_length = self.getLength(slow)
#                 print(cycle_length)
#                 break
#         else: # Important - while-else clause in case there is no cycle
#             return None
#         return self.findStart(head, cycle_length)
        
#     def findStart(self, head, cycle_length):
#         ptr1, ptr2 = head, head
#         while cycle_length:
#             ptr2 = ptr2.next
#             cycle_length -= 1
#         while ptr1 != ptr2:
#             ptr2 = ptr2.next
#             ptr1 = ptr1.next
#         return ptr1

    
    ## Strat: find where the fast and slow pointers meet, if start of cycle is at pos m, and fast and slow meet at k steps from m:
    
    # we know that 
    # dist(fast) = 2d(slow)
#     m + xn + k = 2 (m + yn + k)
#     m + k = (x - 2y) n
#     m + k is a multiple of n
    
#     moving m steps by slow pointer from the start is equal to moving n-k steps for fast pointer from kth point in cycle. 
    