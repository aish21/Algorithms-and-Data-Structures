"""
> Finds the minimum element in the unsorted part of the array that
> Swaps with the first element of the array (unsorted)
> Sorted grows from left to right 
> Not stable (space complexity)
> Worst, Average, Best Case - O(n^2)
"""

def SelectionSort(list):
    for i in range(len(list)):
        minimumIndex = i
        for j in range(i+1, len(list)):
            if(list[minimumIndex] > list[j]):
                minimumIndex = j
        # Swap
        list[i], list[minimumIndex] = list[minimumIndex], list[i]
    return list
