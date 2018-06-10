#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero 
#elements.
#
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#
#Note:
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        count = len(nums)
        nums[:] = [num for num in nums if num]
        nums += [0] * (count - len(nums))
