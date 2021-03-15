## Edge-cases
# - 0 length array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        output = [-1,-1]
        for idx in range(len(nums)):
            if nums[idx] > target:
                break
            elif nums[idx] == target:

                # When the target variable is first encountered
                if output[0] == -1:
                    # Assign target variable to both start and end (in case not encountered again)
                    output[0] = idx
                    output[1] = idx
                else:
                    output[1] = idx

        return output
