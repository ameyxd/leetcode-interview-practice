class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
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