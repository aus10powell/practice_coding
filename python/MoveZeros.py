# Steps:
#   1: Use a brute-force method using addtional space
#   2: Modify the brute-force method to NOT use additional space

# Assumptions/Considerations for extreme cases
#   - Only ints
#   - Only zeros

# Solution: Faster than 22.9

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # array for storing non-zero numbers
        num_zeros = nums.count(0)
        for zero in range(num_zeros):
            nums.remove(0)

        # add on zeros to end of new array
        nums += [0 for _ in range(num_zeros)]

        return nums


## Much better Solution: 96% faster
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)

        j=0
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1

        for i in range(j,n):
            nums[i]=0
