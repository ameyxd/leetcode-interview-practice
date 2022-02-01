# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Get middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse nodes from slow to end
        second = slow.next
        
        # End of first half of the linked list will be new end node
        slow.next = None
        prev = None
        
        # Reverse second part
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge two halves together: prev is new head of second list
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2