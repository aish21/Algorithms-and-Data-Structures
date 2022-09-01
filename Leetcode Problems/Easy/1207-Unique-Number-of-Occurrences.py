'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countDict = Counter(arr)
        numCount = set()
        for x in countDict.values():
            if x in numCount:
                return False
            else:
                numCount.add(x)
        return True