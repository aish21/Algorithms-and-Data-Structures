# Python implementation of Quicksort algorithm

# Quicksort algorithm
def quicksort(array, low, high):
    if low < high:
        pv = divAcon(array, low, high)

        # Left of Pivot
        quicksort(array, low, pv - 1)

        # Right of Pivot
        quicksort(array, pv + 1, high)

# Divide and Conquer algorithm
def divAcon(array, low, high):
    # Rightmost element
    pivot = array[high]

    # Second pointer
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1 # this is where the partition is done

# Driver code
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quicksort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)