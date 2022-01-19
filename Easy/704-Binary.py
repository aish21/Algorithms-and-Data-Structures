'''
- List is ordered
- Declare 2 pointers - start and end of the list
- Iterate while start <= end
- Get middle value
- Compare values - if it is equal, return index
- If middle < target - move start to middle + 1
- If middle > target - move end to middle - 1
- Else return -1

Time - O(logn)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end  = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2

            if(nums[middle] == target):
                return middle
            elif(nums[middle] < target):
                start = middle + 1
            elif(nums[middle] > target):
                end = middle - 1
        
        return -1


