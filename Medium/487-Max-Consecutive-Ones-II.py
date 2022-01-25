class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, prev, curr = 0, 0, 0
        for num in nums:
            if num == 0:
                result = max(result, prev+curr+1)
                prev, curr = curr, 0
            else:
                curr += 1
        return min(max(result, prev+curr+1), len(nums))