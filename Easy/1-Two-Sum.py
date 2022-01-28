'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = {}
        for i in range(len(nums)):
            if(target - nums[i] in required):
                return [required[target - nums[i]],i]
            else:
                required[nums[i]] = i

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            if(nums[start] + nums[end] == target):
                return [start, end]
            
            elif(nums[start] + nums[end] < target):
                start += 1
                
            elif(nums[start] + nums[end] > target):
                end -= 1
                
        return []