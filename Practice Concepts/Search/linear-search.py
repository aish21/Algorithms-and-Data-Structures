# Pythonn implementation of Linear Search Algorithm

def linearSearch(array, x):
    for i in range(len(array)):
        if(array[i] == x):
            return i
    return -1 

# Driver Code
array = [2, 4, 0, 1, 9]
x = 1
result = linearSearch(array, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)