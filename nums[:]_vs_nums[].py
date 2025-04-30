# Move Zeroes

# Theres is a difference in nums[:] and nums[]

# nums[:] = first+last :-> Here we are replace the nums array in place
# nums[] =  first+last  :-> here we are declaring a nums array inside the funtion, but outside the function it remains unchanged

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros=[]
        integers=[]
        for num in nums:
            if num != 0:
                integers.append(num)
            else:

                zeros.append(num)
        nums[:] = integers+zeros
        
        return nums
