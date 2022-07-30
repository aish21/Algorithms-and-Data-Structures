# Python implementation of Radix Sort Algorithm

# Using Counting Sort to sort the elements on the basis of significant places
def countingsort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate the count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

# Radix Sort
def radixsort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingsort(array, place)
        place *= 10

# Driver Code
data = [121, 432, 564, 23, 1, 45, 788]
radixsort(data)
print(data)