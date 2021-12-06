"""
> Requires list to be ordered
> Uses divide and conquer approach
> Check half, if element less than half, then must be on the left.
> Continue this process until the element is found
> Two approaches - iterative and recursive
> Time complexity is O(log(n))
"""

def BinarySearch_Iterative(list, item):
    low = 0
    high = len(list) - 1
    mid = 0
    itemFound = False

    while(low <= high) and not itemFound:
        mid = low + (high - low)/2

        if(list[mid] < item):
            low = mid + 1

        elif(list[mid] > item):
            high = mid - 1
        
        else:
            itemFound = True
            return itemFound, mid
    
    return itemFound

def BinarySearch_Recursive(list, item, low, high):
    itemFound = False
    
    if(low > high):
        return itemFound
    mid = low + (high - low)/2
    if(list[mid] < item):
        BinarySearch_Recursive(list, item, mid + 1, high)
    elif(list[mid] > item):
        BinarySearch_Recursive(list, item, low, mid - 1)
    else:
        itemFound = True
        return mid, itemFound

