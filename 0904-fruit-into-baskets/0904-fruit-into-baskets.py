class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        left, right = 0, 0
        c = defaultdict(int)
        for right, fruit in enumerate(fruits):
            c[fruit] += 1
            while len(c) > 2:
                c[fruits[left]] -= 1
                if c[fruits[left]] == 0:
                    del c[fruits[left]]
                left += 1
            maxFruits = max(maxFruits, right - left + 1)
            
        return maxFruits