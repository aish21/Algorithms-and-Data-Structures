'''
Approach: Use 2 pointers for O(N) complexity
The array given is sorted, which is why we use 2 pointers for the negative portion 
as well as the positive portion of the array (since negative squares -> positive)
The left pointer goes through the negative portion, and the right pointer goes through
the positive portion. If the absolute value is lesser in comparison, that value is then 
squared and put in the result list.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * (len(nums))
        left = 0
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if(abs(nums[left]) < abs(nums[right])):
                sq = nums[right]
                right = right - 1
            else:
                sq = nums[left]
                left = left + 1
            result[i] = sq * sq
        
        return result