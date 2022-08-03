class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        # If I know the first number in one of the group, I know the whole group.
        # Smallest number can only be a part of one group of groupSize size
#         count = {}
#         for n in hand:
#             count[n] = 1 + count.get(n, 0)
        
#         hand.sort() # Or use minHeap to pull out smallest value
        
#         i = 0
#         while i < len(hand):
#             first = hand[i]
#             # Make groups
#             for i in range(groupSize):
#                 nextNum = i + first
#                 if nextNum not in count: # Value we are looking for isn't available to use
#                     print(nextNum)
#                     return False
#                 count[nextNum] -= 1
#                 # Remove the value from the counter if it has been exhausted from the count dict
#                 if count[nextNum] == 0:
#                     del count[nextNum]
#             # set value for first position in next group as the next valid entry
#             while i < len(hand) and hand[i] not in count:
#                 i += 1
#         return True

        n, W = len(hand), groupSize
        counter = Counter(hand) # O(n)
        hand.sort() # O(nlogn)
        i, n = 0, len(hand)
        while i < n: # O(n)
            cur = hand[i]
            for j in range(W): # O(W)
                if cur+j not in counter:
                    return False
                counter[cur+j] -= 1
                if counter[cur+j] == 0:
                    del counter[cur+j]
            while i < n and hand[i] not in counter:
                i += 1
        return True