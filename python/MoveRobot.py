### Assumptions/Edge Cases
# - All characters are upper case

## Steps:
# - Only need to know if x,y coords are both 0

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        # length of the string may be 0
        if len(moves) == 0:
            return True
        
        # if number of moves > 0
        else:
            x = 0
            y = 0

            ##################################
            # move the robot
            ##################################
            for move in moves:
                if move == 'U':
                    y += 1
                elif move == 'D':
                    y -= 1
                elif move == 'L':
                    x -= 1
                else:
                    x += 1
                    
            if (x == 0) and (y == 0):
                return True
            else:
                return False