class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Stack
        # If two cars reach the destination at or before the same time, they become a fleet
        # Since each block may be traveling at a different speed at a later time, you have to calculate in reverse order, i.e., go from car closest to target to farthest
        # Sort by position
        
        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(pair)[::-1]:
            timeToReachTarget = (target - p) / s
            stack.append(timeToReachTarget)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # These two cars collide
                stack.pop() # simply stop considering the current car - it becomes a fleet
        return len(stack)