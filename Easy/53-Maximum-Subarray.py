'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, temp = nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            if(temp > ans):
                ans = temp
        return ans