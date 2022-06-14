# Insertion Sort Algorithm

def insertionSort(arrayToBeSorted):
    for i in range(1, len(arrayToBeSorted)):
        key = arrayToBeSorted[i]

        j = i - 1 
        while j >= 0 and key < arrayToBeSorted[j]:
            arrayToBeSorted[j + 1] = arrayToBeSorted[j]
            j -= 1 
        arrayToBeSorted[j + 1] = key
    return arrayToBeSorted

arrayToBeSorted = [10, 8, 12, 19, 6, 2]
print('Original List:', arrayToBeSorted)
print('Sorted List (via Insertion Sort): ', insertionSort(arrayToBeSorted))
