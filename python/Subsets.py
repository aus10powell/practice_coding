#######################################################
# Mine: Faster than 82.45%
# Complexity:
#  O (N * r choose N)
#######################################################

import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        combinations = [[]]
        for r in range(1,len(nums) + 1):
            sub_combo = list(itertools.combinations(nums,r))
            combinations += sub_combo
        return combinations
