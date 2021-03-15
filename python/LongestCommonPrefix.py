#########################
# Solution: not mine faster than 58%
# Time Complexity: O(n^2)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) is 0:
            return ''

        answer = ''
        for i,letter in enumerate(strs[0]):
            for s in strs[1:]:
                if letter != s[i:i+1]:
                    return answer
            answer += letter
        return answer
