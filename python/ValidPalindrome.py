import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Returns whether a string is a Palendrome or not.
            * All alpha-numeric characters are ignored
            * Solution is O(N)
        """
        # convert string to lower
        s = s.lower()

        s = re.sub(r'\W', '', s)
        s = re.sub('_','',s)

        answer = False

        if len(s) <= 1:
            answer = True
            return answer


        else:
            for i in range(int(len(s) / 2)):
                if s[i] != s[-(i+1)]:
                    answer = False
                    break
                else:
                    answer = True
                    continue

            return answer
