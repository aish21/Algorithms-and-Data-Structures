class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr) < 3):
            return False
        
        prev = None
        max_index = None
        for i, num in enumerate(arr):
            if prev != None and num <= prev:
                break

            prev = num
            max_index = i
        
        
        if max_index == 0 or max_index == len(arr) - 1:
            return False
        
        for i, num in enumerate(arr[max_index + 1:]):
            if num >= prev:
                print (num, prev)
                return False
            
            prev = num
            
        return True