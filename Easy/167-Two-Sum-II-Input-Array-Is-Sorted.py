class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start <= end:
            summation = numbers[start] + numbers[end]
            
            if(summation == target):
                return [start + 1, end + 1]
            elif(summation < target):
                start += 1
            else:
                end -= 1
        
        return [-1, -1]