# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        ansHead = ListNode(0)
        curr = ansHead
        carry = 0
        while p1 or p2:
            sumVal = 0
            if p1:
                sumVal += p1.val
                p1 = p1.next
            if p2:
                sumVal += p2.val
                p2 = p2.next
            sumVal += carry
            carry = sumVal // 10
            curr.next = ListNode(sumVal % 10)
            curr = curr.next
                    
        if carry:
            curr.next = ListNode(carry)
        
        return ansHead.next