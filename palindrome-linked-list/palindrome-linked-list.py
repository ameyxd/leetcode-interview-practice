# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        middle_head = self.reverse(slow)
        middle_head_copy = middle_head
        
        while head and middle_head:
            if head.val != middle_head.val:
                break
            head = head.next
            middle_head = middle_head.next
            
        self.reverse(middle_head_copy)
        
        if head is None or middle_head is None:
            return True
        
        return False