class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeroMap = {} # store index and value wherever element is non-zero
        for i, n in enumerate(nums):
            if n:
                self.nonzeroMap[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, n in self.nonzeroMap.items():
            if i in vec.nonzeroMap:
                result += n * vec.nonzeroMap[i]
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)