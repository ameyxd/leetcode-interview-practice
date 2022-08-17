class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # At every point there are two options, either add y to x or add x to y: Recursive approach will be O(2^n)
        # Instead, you can try going from the target to the source, since we know if x > y, that means we need to subtract y from x
        
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            #  source X has been reached, check if source y can be reached, if the difference in source and target y is div by x, we can get to that y
            if tx == sx and (ty - sy) % tx == 0:
                return True
            if ty == sy and (tx - sx) % ty == 0:
                return True
            
            if tx > ty:
                # tx -= ty
                tx %= ty # Optimization to skip levels
            else:
                # ty -= tx
                ty %= tx
        
        return False