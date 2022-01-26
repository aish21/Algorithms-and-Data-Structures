class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        exp = set(range(1, length + 1))
        
        for num in nums:
            if(num in exp):
                exp.remove(num)
        
        return exp