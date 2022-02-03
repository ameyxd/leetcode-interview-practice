# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
ListNode.__eq__ = lambda self, other : self.val == other.val 
ListNode.__lt__ = lambda self, other : self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Solution 1 : Merge like in merge sort (divide and conquer) using the merge 2 lists logic
        
#         if not lists or len(lists) == 0:
#             return None
        
#         while len(lists) > 1:
#             mergedLists = []
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if (i + 1) < len(lists) else None
#                 lists[i] = mergedLists(self.mergeTwoLists(l1, l2))
#             # lists = mergedLists
#         return lists[0]
        
#     def mergeTwoLists(self, l1, l2):
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2.val
#                 l2 = l2.val
#             tail = tail.next

#         if l1:
#             tail.next = l1
#         elif l2:
#             tail.next = l2
#         return dummy.next

        # Solution 2: Heap
        heap = []
        for l in lists:
            if l:
                heap.append((l.val, l))
        heapq.heapify(heap)
        dummy = ListNode(None)
        ptr = dummy

        while heap:
            val, node = heapq.heappop(heap)
            ptr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            ptr = ptr.next
        
        return dummy.next
            
            
        
#         import heapq

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         heap = []
        
#         for li in lists:
#             if li:
#                 heap.append((li.val, li))
#         o(k)
#         heapq.heapify(heap)
#         o(k + nlogk)
#         merge_ptr = merge_head = None
#         #nlogk
#         while heap:
#         		#logk
#             val, node = heapq.heappop(heap)
            
#             if merge_head is None:
#                 merge_head = merge_ptr = node
#             else:
#                 merge_ptr.next = node
#                 merge_ptr = merge_ptr.next
            
#             if node.next:
#             		#logk
#                 heapq.heappush(heap, (node.next.val, node.next))
        
#         return merge_head