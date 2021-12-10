'''
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. 
If it is, return the index of the largest element, or return -1 otherwise.
'''

def dominantIndex(self, nums: List[int]) -> int:
    largest = max(nums)
    index = nums.index(largest)
    temp = [val*2 for val in nums]
    temp.pop(index)
    count = 0
    for i in range(len(temp)):
        if(largest >= temp[i]):
            count += 1
    if(count == len(temp)):
        return index
    else:
        return -1