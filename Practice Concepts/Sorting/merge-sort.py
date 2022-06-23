# Python implementation of Merge Sort algorithm

def mergeSort(inputArr):
    if(len(inputArr)) > 1:

        # Point of division for the array into subarrays
        r = len(inputArr)//2
        subA1 = inputArr[:r]
        subA2 = inputArr[r:]

        # Recursively divide the array until only single elements are left, and sort them
        mergeSort(subA1)
        mergeSort(subA2)

        i = j = k = 0

        # Until we reach the end of either of the sub arrays, pick the smaller amongst the 2 and place in array
        while i < len(subA1) and j < len(subA2):
            if(subA1[i] < subA2[j]):
                inputArr[k] = subA1[i]
                i += 1
            else:
                inputArr[k] = subA2[j]
                j += 1
            k += 1
        
        # Place remaining elements in the output array
        while i < len(subA1):
            inputArr[k] = subA1[i]
            i += 1
            k += 1
        
        while j < len(subA2):
            inputArr[k] = subA2[j]
            j += 1
            k += 1

# Driver code
inputArr = [5, 10, 4, 2, 3, 18, 15, 22]
mergeSort(inputArr)
for l in range(len(inputArr)):
    print(inputArr[l])