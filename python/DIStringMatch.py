## Assumptions/Limiting cases

## Approach
#   Count the number of I's and D's
#   Use those codes to start with the highest (or lowest number)

## Solution: Mine 93%


class Solution:
    def diStringMatch(self, S: str) -> List[int]:


        output = []
        i = 0
        d = len(S)


        for s in S:
            if s == 'I':
                output.append(i)
                i += 1
            else:
                output.append(d)
                d -= 1

        if S[-1] == 'D':
            output.append(d)
        else:
            output.append(i)

        return output
