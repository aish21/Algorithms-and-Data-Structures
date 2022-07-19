<h1 align="center">
  <br>
  Algorithms and Data Structure: A Comprehensive Guide
  <br>
</h1>

<h4 align="center">My notes on concepts covering algorithms and data structures</h4>

<p align="center">
    <a href="#introduction-to-data-structures">Introduction to Data Structures</a> •
    <a href="#introduction-to-algorithms">Introduction to Algorithms</a> •
    <a href="#sorting-algorithms">Sorting Algorithms</a> •
    <a href="#search-algorithms">Search Algorithms</a> •
    <a href="#trees">Trees</a> •
    <a href="#graphs">Graphs</a> •
</p>

## Introduction to Data Structures
<p align="center">
    <a href="#basics">Basics</a> •
    <a href="#stacks">Stacks</a> •
    <a href="#queues">Queues</a> •
    <a href="#linked-list">Linked List</a> •
    <a href="#hash-tables">Hash Tables</a> •
    <a href="#heaps">Heaps</a>
</p>

### Basics
* Data Structures are storage units used to store and organize data - done in a way so that data can be accessed and updated efficiently
* Types of data structures - Linear and Non-Linear
* Linear Data Structures - 
    - Elements are arranged in sequential order 
    - Easier to implement for less complex use cases
    - Arrays: Elements are arranged in continuous memory - all the elements that can be stored in an array are of the same type.
    - Stacks: Elements stored in LIFO (Last In First Out)
    - Queues: Elements stores in FIFO (First In First Out)
    - Linked List: Elements connected through a series of nodes, where each node contains item and address to the next node

* Non-Linear Data Structures - 
    - Non-sequential 
    - Arranged in hierarchical order - one element connected to one or multiple elements
    - Graphs: Each node is called a vertex and vertices are connected to each other via edges.
    - Trees: Similar to graphs, but there can only be one edge between two vertices.

| Linear Data Structures | Non-Linear Data Structures |
| :--------------------: | :-------------------------:| 
| Sequential             | Non-Sequential             | 
| All items present in single layer | In multiple layers | 
| Traversed in a single run | Requires multiple runs | 
| Inefficient memory utilization | Relatively efficient memory utilization |
| Time complexity increases with data | Time complexity remains the same | 

### [Stacks](/Practice%20Concepts/Data%20Structures/stacks.py)
* Linear Data Structure that follows the principle of LIFO - Last In First Out.
* Putting an item on top of the stack is known as 'push' and removing an item is known as 'pop'.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/PUSH-POP.png)

* PUSH: Add an element to the top of the stack
* POP: Remove an element from the top of the stack
* IsEmpty: Check if the stack is empty           
* IsFull: Check if the stack is full 
* PEEK: Check the value of the top element in the stack without removing it
* Working of stacks - 
    - Pointer variable TOP: keep track of the top element in the stack
    - Stack initialization, TOP is set to -1. It is then compared back to -1 to check if it is empty as well.
    - During PUSH, increment the value of TOP by 1 and place the element at the index of the value pointed by TOP.
    - During POP, return the value of TOP first (element at that index) and then decrease the value of TOP by 1.
    - Before pushing, check if the stack is full and before popping check if the stack is empty.
* PUSH and POP operations take constant time - O(1).
* Stack Applications: String reversals, compilers, browser (saving previously visited URLs)

### [Queues](/Practice%20Concepts/Data%20Structures/Queue.py)
* Linear data structure that follows FIFO - First In First Out rule - the item that goes in first comes out first
* Putting items in queue is known as enqueue and removing items from queue is known as dequeue.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/enq-dq.png)

* ENQUEUE: Add an element at the end of the queue
* DEQUEUE: Remove an element from the front of the queue
* IsEmpty: Check if the queue is empty
* IsFull: Check if the queue is full
* PEEK: Check the value of the first element in the queue without removing it
* Queue Operations - 
    - Pointer variables: FRONT and REAR (first element and last element tracked respectively)
    - Initially both values are -1 
    - ENQUEUE - Check if the queue is full, for first value, set FRONT = 0, increment REAR by 1, add the element pointed to by the REAR pointer
    - DEQUEUE - Check if the queue is empty, return the value pointed by FRONT, increment FRONT by 1, for final value, reset FRONT and REAR to -1.
* Limitations: We can only add to index 0 after all the elements have been dequeued (see circular queue)
* ENQUEUE and DEQUEUE operations take constant time - O(1). pop(N) in python may take O(n) depending on the position of the item to be popped.
* Applications: CPU Scheduling, File System buffers, interrupts in real time systems.

* Types of Queues:

    - [Circular Queue](/Practice%20Concepts/Data%20Structures/CircularQ.py)
        - Like regular queue, but the last element is connected to the first element, solving the limitation stated earlier (non-usable empty space).
        - Works in the process of circular increment - modulo division with the queue size
        - Same initialization of FRONT and REAR pointer variables
        - ENQUEUE: FRONT is set to 0, REAR is circularly incremented by 1, if it reaches the end, it would be at the start of the queue, then add to the position pointed to by REAR.
        - DEQUEUE: Return value pointed by FRONT, circularly increase FRONT by 1, for last element, reset the FRONT and REAR values to -1
        - IsFull conditions: FRONT == 0 && REAR == SIZE - 1, FRONT = REAR + 1 
        - Complexity: O(1)

    - Priority Queue (TODO)
        - Each element is linked with a priority value - served on the basis of their priority.
        - If elements have the same priority, they are then served according to their order in the queue.
        - Does not follow FIFO - follows rule of priority
        - Implemented using binary heap (refer to heap below)
    
    - Deque (Double Ended Queues)
        - TODO

### [Linked List](/Practice%20Concepts/Data%20Structures/singly-linked-list.py)
* Linear data structure that includes a series of connected nodes - each node stores the data and the address of the next node.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/linked-list.png)

* HEAD: Address of the first node 
* Last node identified as the node that points to its next portion as NULL
* Types of Linked Lists: Singly, Doubly, Circular
* The power of linked list comes from the ability to break the chain and rejoin it. Doing something similar in an array would have required shifting the positions of all the subsequent elements.
* Space Complexity: O(n)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/linked-list-complexity.png)

* Applications - Dynamic memory allocation, stacks and queues, hash tables
* Linked List operations:
    - Traversal: Access each element of the linked list
    - Insertion: Add a new element to the linked list
    - Deletion: Removes the existing elements from the linked list
    - Search: Find a node in the linked list
    - Sort: Sort the nodes of a linked list

* Doubly Linked List: Add a pointer to the previous node, therefore can traverse either direction - forward or backward.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/DLL.png)

* Circular Linked List: Last element is linked to the first element, forming a loop. This can be both a doubly linked list or a singly linked list.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/CLL.png)

### [Hash Tables](/Practice%20Concepts/Data%20Structures/hash-table.py)
* Data structure that stores data in key-value pairs - 
    - Key: Unique integer that is used for indexing the values
    - Value: Data associated with the Keys
* In a hash table, the new index is processed using keys, then the element corresponding to that key is stored in the index - Hashing.
* Hashing is a technique of mapping a large set of arbitrary data to tabular indexes using a hashing function. It allows lookups, updating and retrieval operation to occur in a constant time - O(1), that is it is not dependent on the size of the data
* Let k = hey and h(x) = hashing function. h(k) will give us a new index to store the element associated with key k. 

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/h(x).png)

* Hash Collision - When the hash function generates the same index for multiple keys. This can be resolved by - 
    - Collision resolution by chaining:
        - If the hash function produces the same index for multiple elements, these elements are stored in the same index using a doubly linked list.
        - If x is the index for multiple elements, then it contains a pointer pointing to the head of the list. If there are no elements, x contains NIL.
    - Open Addressing: Linear/Quadratic Probing and Double Hashing:
        -  Open addressing does not store multiple elements into the same slot - each slot is either filled with a single key or left NIL.
        - Technique 1: Linear Probing:
            - Collision is resolved by checking the next slot.
            - h(k, i) = (h′(k) + i) mod m; i is the set of index values and h'(k) is the new hash function.
            - Value of i is incremented linearly.
            - Problem: Cluster of adjacent slots filled - all must be traversed when inserting a new element.
        - Technique 2: Quadratic Probing:
            - Spacing between the slots is increased
            - h(k, i) = (h′(k) + c1i + c2i<sup>2</sup>) mod m
            - c1 and c2 are positive auxiliary constants
        - Technique 3: Double Hashing:
            - If a collision occurs after applying a hash function h(k), then another hash function is calculated for finding the next slot
            - h(k, i) = (h1(k) + ih2(k)) mod m

* Good Hash Functions: May not prevent collisions but can reduce the number of collisions.
    - Division Method: 
        - If k is a key and m is the size of the hash table, the hash function h() is calculated as h(k) = k mod m
        - The value of m must not be the powers of 2 - will always get lower order p bits.
    - Multiplication Method: 
        - h(k) = ⌊m(kA mod 1)⌋
        - kA mod 1 gives the fractional part kA
        - ⌊ ⌋ gives the floor value
        - A is any constant. The value of A lies between 0 and 1. But, an optimal choice will be ≈ (√5-1)/2 (Knuth)
    - Universal Hashing: hash function is chosen at random independent of keys


## Introduction to Algorithms
* Algorithms - Finite steps/instructions followed to solve a computational problem in an efficient manner.
* Importance of algorithms - 
    - Different algorithms aid in solving problems in an efficient manner.
    - Improves run time/speed of programs

* Characteristics of algorithms - 
    - Finite number of steps
    - Clear and easy to understand
    - Efficient in utilization of resources

* Factors that determine an algorithm's efficiency: Time complexity and Space complexity
* Space Complexity - 
    - Calculating the amount of space consumed by an algorithm during the course of its execution.
    - Broadly classified into fixed/constant complexity and linear complexity
    - Fixed/Constant: Size of space consumed will not increase with increase of input size.
    - Linear: Space consumed increases with increase of input size - O(n).
    - Take note of the number of variabled during calculation of space complexity

* Time Complexity - 
    - Concentrate on the number of statements executed for calculation of time complexity.
    - Loops - will be executed 'len + 1' times - it will also calculate till, after the condition is false
    - Inside the loop - 'len' times execution 
    - Increasing order of time complexity - O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n<sup>2</sup>) < O(n<sup>3</sup>) < O(2<sup>n</sup>) < O(3<sup>n</sup>) < O(n<sup>n</sup>)

* Asymptotic Notations - 
    - Mathematical functions used to calculate the running time as well as the order of growth of algorithms.
    - Running time refers to the time taken for the computer to run all the statements in an algorithm.
    - Rate of growth refers to how the algorithm will behave when a large amount of input is given.
    - Types: Big O (worst case - tight upper bound), Big Omega (lower bound), Big Theta(average case)

* [Big O](/extras/Basics/Big-O%20Notation.jpeg) - 
    - Big O notation is generally used to calculate the complexity of an algorithm - how the algorithm will perform when the input size is increased
    - To say a function f(n) is equal to O(g(n)), if there is a constant “c” and “n0” such that the function f(n) will always be less that “c * g(n)”, can be written as “f(n) < c*g(n)" - the function f(n) will not go above the function g(n) for a large value of n. Hence we can consider the function “g(n)” as upper bound for the function f(n)

* [Big Omega](/extras/Basics/Omega%20Notation.jpeg) and [Theta](/extras/Basics/Theta%20Notation.jpeg) - 
    - Omega - For a function f(n) is equal to Ω(g(n)) if there exist a constant C and n0 such that f(n) is always greater than C(g(n)). i.e. f(n) > C(g(n)) or C(g(n)) < f(n) (Best Case)
    - Theta - For a function f(n) is equal to Ø(n) if a function f(n) is greater than C1 g(n) and is less than C2g(n) for all n>= 0. It means that the function f(n) will always be in-between C1*g(n) and C2*g(n). It can be shown in formula as :  C1*g(n) <= f(n) <= C2*g(n) (Average Case)

## Sorting Algorithms
* [Bubble Sort](/Practice%20Concepts/Sorting/bubble-sort.py) - 
    - Bubble Sort will sort by checking if the next element is greater than the present element - if greater then it will swap the elements.
    - Use of 2 loops - outer and inner 
    - Each element is compared to its adjacent element - if current is greater, then we swap them
    - At the end of the first iteration, the largest element will be at the end, the second largest will be at the n - 1 position
    - Outer loop is to loop n times and inner loop is for swapping
    - In place sorting
    - Worst Case: O(n<sup>2</sup>)
    - Best Case: O(n)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Bubble-sort.gif)

* [Selection Sort](/Practice%20Concepts/Sorting/selection-sort.py) - 
    - Selection Sort is a sorting technique where the smallest element is taken from the array and placed at the first index - this is repeated for the remaining elements. 
    - Get the smallest element from the array, exchange it with the first index element
    - Second smallest element swap with second index position, and so forth 
    - Need of 2 loops - outer loop iterate all the array elements one by one, inner loop - here the element from the outer loop is checked against all the elements from inner loop. If a smaller element is found, then that element will be replaced with the index of outer loop
    - Best, Worst Case: O(n<sup>2</sup>)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Selection-Sort.gif)

* [Insertion Sort](/Practice%20Concepts/Sorting/insertion-sort.py) - 
    - Insertion Sort is an efficient algorithm for sorting a small number of elements.
    - In-place sorting - rearranges the elements in place.
    - Keys: Numbers that we wish to sort
    - Divide array into sorted and unsorted elements, select first unsorted element (key), swap the sorted elements to the right to create the correct position and shift the unsorted element (key), advance marker to right (next key)
    - Best Case: O(n)
    - Worst Case: O(n<sup>2</sup>)
    
    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Insertion-Sort.gif)

* [Merge Sort](/Practice%20Concepts/Sorting/merge-sort.py) - 
    - Based on the divide and conquer strategy
    - Divide: Divide the array into half, and continue to do so with the resultant arrays until only single elements are left
    - Conquer: Sort the left part and right part of the array recursively
    - Combine: Combine the left and right arrays to form one complete, sorted array
    - External Sorting, Stable
    - Best Case, Worst Case and Average Case: O(nlogn)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Merge-Sort.gif)

    
