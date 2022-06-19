# Python implementation of Bubble Sort algorithm

def bubbleSort(inputArr):
    # Do not go through if array is sorted
    swapped = False 

    # Outer Loop - for checking all the elements
    for i in range(len(inputArr) - 1):
        # Inner Loop - for swapping
        for j in range(0, len(inputArr) - i - 1):
            if(inputArr[j] > inputArr[j + 1]):
                swapped = True
                inputArr[j], inputArr[j + 1] = inputArr[j + 1], inputArr[j]
            
        if not swapped:
            # Exit the main loop if no swap was needed to be made
            return

inputArr = [5, 10, 4, 2, 3, 18, 15, 22]
bubbleSort(inputArr)
for k in range(len(inputArr)):
    print(inputArr[k])