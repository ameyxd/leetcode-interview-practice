class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Think of matrix as n sorted rows/lists, use minheap
        ROWS, COLS = len(matrix), len(matrix[0])
        heap = [(matrix[r][0], r, 0) for r in range(ROWS)]
        heapq.heapify(heap)
        
        while k:
            val, row, col = heapq.heappop(heap)
            col += 1
            if col in range(COLS):
                heapq.heappush(heap, (matrix[row][col], row, col))
            k -= 1
        return val