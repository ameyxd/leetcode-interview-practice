class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key = lambda num: abs(x - num))
        
        result = []
        
        for i in range(k):
            result.append(sorted_arr[i])
        
        return (sorted(result))
            
    