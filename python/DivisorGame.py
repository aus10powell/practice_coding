## Solution beats 85%
## Approach
# - Difficult to solve deterministically. Better to solve in analytically.

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N%2==0:
            return True
        else:
            return False
