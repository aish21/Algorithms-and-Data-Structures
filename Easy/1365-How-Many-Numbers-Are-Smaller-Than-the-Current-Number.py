'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        checkLessNum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] - nums[j] > 0):
                    checkLessNum += 1
            output.append(checkLessNum)
            checkLessNum = 0
        return output
        