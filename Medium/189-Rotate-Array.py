
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        for i in range(len(nums) - 1, (len(nums) - 1) - k, -1):
            nums.insert(0, nums[right])
            nums.pop()
