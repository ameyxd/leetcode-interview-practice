class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Since bob can always get the smallest pile, and you don't want it, randomized process of picking the three piles can be done so that it maximizes your coins
        # Sort list, iterate two from right one from left
        
        piles.sort()
        res = 0
        n = len(piles)
        for i in range(n//3, n, 2):
            print(piles[i])
            res += piles[i]
        return res
    
#         sorted_piles = sorted(piles)
#         end_idx = len(piles) - 1
#         max_total = 0
#         for i in range(len(piles )// 3):
#             # Bob's val, Alice's val, our val
#             # triplet = (sorted_piles[i], sorted_piles[end_idx - (2 * i)], sorted_piles[end_idx - (2 * i) - 1])
#             my_val = sorted_piles[end_idx - (2 * i) - 1]
#             max_total += my_val
#         return max_total