"""
> Also known as linear search
> Check for the desired element in sequence until it is found or the 
list is exhausted.
> Need not be Ordered.
> Time complexity is O(n)
"""

def SequentialSearch(list, item):
    index = 0
    itemFound = False

    while index < len(list) and not itemFound:
        if list[index] == item:
            itemFound = True
        else:
            index += 1
    
    return index, itemFound