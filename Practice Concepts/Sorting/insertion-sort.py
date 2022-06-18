# Insertion Sort Algorithm

def insertionSort(arrayToBeSorted):

    # Outer loop - start from the second element in the list
    for i in range(1, len(arrayToBeSorted)):
        # Element to be sorted
        key = arrayToBeSorted[i]

        # Move elements that are greater than the key one place to the right
        # Checking for the comparison from right to left
        j = i - 1 
        while j >= 0 and key < arrayToBeSorted[j]:
            arrayToBeSorted[j + 1] = arrayToBeSorted[j]
            j -= 1 
        arrayToBeSorted[j + 1] = key
    return arrayToBeSorted

arrayToBeSorted = [10, 8, 12, 19, 6, 2]
print('Original List:', arrayToBeSorted)
print('Sorted List (via Insertion Sort): ', insertionSort(arrayToBeSorted))
