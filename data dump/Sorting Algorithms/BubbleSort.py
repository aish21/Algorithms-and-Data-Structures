"""
> Compares a pair of elements in one iteration
> Moves larger to the right
> Sorted grows from right to left 
> Worst, Average Case - O(n^2)
> Best case - O(n)
"""

def BubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if(list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]

    return list