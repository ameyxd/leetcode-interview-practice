class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        n = len(fruits)
        max_fruits = 0
        counter = defaultdict(int)
        
        for right, f in enumerate(fruits):
            counter[f] += 1
            while len(counter) > 2:
                # shrink left pointer
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0: # remove from counter
                    del counter[fruits[left]]
                left += 1
                
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits