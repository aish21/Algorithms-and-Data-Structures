class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        maxV = max(nums)
        
        if(len(nums) < 3):
            return maxV
        
        nums.remove(maxV)
        nums.remove(max(nums))
        return max(nums)