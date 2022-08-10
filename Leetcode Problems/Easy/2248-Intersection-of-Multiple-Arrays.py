'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
'''
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(i for i in range(1001))
        for num in nums:
            result &= set(num)
        return sorted(list(result))
        