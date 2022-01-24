class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if(nums[i] % 2 != 0):
                odd.append(nums[i])
            else:
                even.append(nums[i])
        return even + odd