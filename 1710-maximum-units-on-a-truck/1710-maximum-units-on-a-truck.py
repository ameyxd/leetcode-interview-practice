class Solution:
    def maximumUnits1(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort by highest number of units
        maxUnits = 0
        boxTypes.sort(key=lambda x: -x[1])
        for box in boxTypes:
            if truckSize < 0:
                break
            numBoxes, units = box[0], box[1]
            maxUnits += min(truckSize, numBoxes) * units
            truckSize -= numBoxes
        return maxUnits

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap, maxUnits = list(), 0
        for box in boxTypes:
            num, units = box
            heapq.heappush(heap, (-units, num))
            
        while heap and truckSize > 0:
            units, num = heapq.heappop(heap)
            maxUnits = maxUnits + (-1 * units * (num if truckSize >= num else truckSize))
            # maxUnits += (-1 * units) * min(truckSize, num)
            truckSize -= num
        return maxUnits
