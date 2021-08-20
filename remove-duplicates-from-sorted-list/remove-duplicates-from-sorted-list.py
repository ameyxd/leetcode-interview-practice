# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        
        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next