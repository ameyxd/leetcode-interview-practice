class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Does robot go to infinity or not
        # After performing all the moves, does it end up in the same place
        # The direction may have changed when you get to the same position, but after 4 turns you are guaranteed to face same direction
        # Execute sequence of instructions 4 times if you end up at start position the robot is bounded
        x, y = 0, 0
        dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} # 0 is north, 1 is east, 2 is south, 3 is west
        facing = 1 # initially facing north
        for i in range(4):
            for char in instructions:
                if char == 'G':
                    x += dirs[facing][0]
                    y += dirs[facing][1]
                if char == 'R': # Do this by seeing how to convert 0 1 2 3 -> 1 2 3 0
                    facing = (facing + 1) % 4
                if char == 'L': # Do this by seeing how to convert 0 1 2 3 -> 3 0 1 2
                    facing = (facing + 3) % 4
        return x == 0 and y == 0