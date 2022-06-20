# Python implementation of Selection Sort algorithm

def selectionSort(inputArr):

    # Outer Loop to traverse through all array elements
    for i in range(len(inputArr)):
        # Set the current value index as the minimum index
        index_of_min = i

        # Inner Loop to find the index of minimum value
        for j in range(i + 1, len(inputArr)):
            if(inputArr[index_of_min] > inputArr[j]):
                index_of_min = j

        inputArr[i], inputArr[index_of_min] = inputArr[index_of_min], inputArr[i]

inputArr = [5, 10, 4, 2, 3, 18, 15, 22]
selectionSort(inputArr)
for k in range(len(inputArr)):
    print(inputArr[k])