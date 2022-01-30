# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        
        p = dummy = ListNode(None)
        dummy.next = head
        
        for i in range(left - 1):
            p = p.next

        tail = p.next
    
        def reverse_int(node, count):
            prev, curr = None, node
            while curr and count:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count -= 1
            return prev, next
            
        new_head, r_next = reverse_int(tail, right - left + 1)
        p.next = new_head
        
        tail.next = r_next
        
        # for i in range(right - left):
        #     temp = p.next
        #     p.next = tail.next
        #     tail.next = tail.next.next
        #     p.next.next = temp
        # return dummy.next
        

        return dummy.next
    
    # Strat: Use dummy node for starting because it makes. Then draw diagram to do the link changes