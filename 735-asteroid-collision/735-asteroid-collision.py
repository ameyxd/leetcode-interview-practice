class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Row of asteroids is stable if new asteroid added on the right is of the same direction
        
        stack = []
        for ast in asteroids:
            # Collision only happens if the incoming asteroid is negative and the top of the stack is positive
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                if diff < 0: # ast wins
                    stack.pop()
                elif diff > 0: # top of stack wins
                    ast = 0
                else: # if both asteroids destroyed
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        
        return stack

    
        