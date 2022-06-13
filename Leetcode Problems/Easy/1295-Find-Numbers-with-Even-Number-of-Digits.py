class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        temp = []
        count = 0
        
        for num in nums:
            temp = [int(i) for i in str(num)]
            if(len(temp) % 2 == 0):
                count += 1
            temp.clear()
            
        return count