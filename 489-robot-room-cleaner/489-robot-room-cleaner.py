# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        # To get back to the original position
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        # DFS backtracking
        def backtrack(x, y, d):
            robot.clean()
            # Explore all 4 directions
            for i in range(4):
                newD = (d + i) % 4
                newX, newY = x + directions[newD][0], y + directions[newD][1]
                if (newX, newY) not in seen and robot.move(): #robot.move is essentially telling us if the new position is valid or not
                    seen.add((newX, newY))
                    backtrack(newX, newY, newD)
                    goBack()
                robot.turnRight()
            
            
        directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)} # Sequence matters, you move in clockwise direction, 0 is up, 1 is right, 2 is down, 3 is left
        seen = set() # record cells visited before
        backtrack(0, 0, 0) # start at up
        