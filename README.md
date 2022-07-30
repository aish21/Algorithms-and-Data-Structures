<h1 align="center">
  <br>
  Algorithms and Data Structures: A Comprehensive Guide
  <br>
</h1>

<h4 align="center">My notes on concepts covering algorithms and data structures, as well as solved Leetcode problems</h4>

<p align="center">
    <a href="#introduction-to-data-structures">Introduction to Data Structures</a> •
    <a href="#trees">Trees</a> •
    <a href="#graphs">Graphs</a> •
    <a href="#introduction-to-algorithms">Introduction to Algorithms</a> •
    <a href="#sorting-algorithms">Sorting Algorithms</a> •
    <a href="#search-algorithms">Search Algorithms</a> •
    <a href="#greedy-algorithms">Greedy Algorithms</a> •
    <a href="#dynamic-programming">Dynamic Programming</a> •
    <a href="#other-algorithms">Other Algorithms</a> •
    <a href="#leetcode-explanation">Leetcode Explanation</a>
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


## Trees
<p align="center">
    <a href="#introduction-to-trees">Introduction to Trees</a> •
    <a href="#binary-tree">Binary Tree</a> •
    <a href="#binary-search-tree">Binary Search Tree</a> •
    <a href="#avl-tree">AVL Tree</a> •
    <a href="#b-tree">B Tree</a> •
    <a href="#red-black-tree">Red Black Tree</a>
</p>

### [Introduction to Trees](/Practice%20Concepts/Trees/tree-traverse.py)
* A non-linear hierarchical data structure that consists of nodes connected via edges.
* For linear data structures, time complexity increases with data size - trees allow quicker and easier access.
* Node: An entity that contains a key or value and pointers to its child nodes. The last nodes of each path are known as leaf/external nodes - no link to child node. Nodes with child nodes - internal nodes.
* Edge: Link between any 2 nodes.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/node-edge.png)

* Root: topmost node of a tree.
* Height (Node): Number of edges from the node to the deepest leaf (longest path from the node to the leaf node)
* Depth (Node): Number of edges from the root to the node.
* Height (Tree): Height of the root node.
* Degree of a Node: Total number of branches of that node
* Forest: Collection of disjoint trees - by cutting the root of a tree.
* Tree traversal: visiting every node in the tree. 
* Use traversal methods that take into account the hierarchical structure of the tree.
* Every tree is a combination of a node carrying data and 2 subtrees.
* Types of Traversal: 
    - Inorder: Visit all the nodes in the left subtree, root node then all the nodes in the right subtree.

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/in-order-traversal.gif)

    - Preorder: Visit root node, visit all the nodes in the left subtree, visit all the nodes in the right subtree. 

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/pre-order-traversal.gif)

    - Postorder: Visit all the nodes in the left subtree, visit all the nodes in the right subtree, visit the root node.

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/post-order-traversal.gif)

### [Binary Tree](/Practice%20Concepts/Trees/binary-tree.py)
* Tree data structure in which each parent node can have at most 2 children. Each node contains - data item, address of left child, address of right child.
* [Full Binary Tree](/Practice%20Concepts/Trees/full-binary-tree.py): 
    - Every parent/internal node has either 2 or no children nodes. 

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/full-binary-tree.png)

    - Also known as a proper binary tree
    - Let i = number of internal nodes | n = total number of nodes | l = number of leaves | λ = number of levels 
    - Number of leaves = i + 1
    - n = 2i + 1
    - l = (n + 1) / 2
    - i = l – 1
    - l is at most 2<sup>λ</sup> - 1

* [Perfect Binary Tree](/Practice%20Concepts/Trees/perfect-binary-tree.py): 
    - Every internal node has exactly 2 child nodes and all the leaf nodes are at the same level. 

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/perfect-binary-tree.png)

    - All internal nodes have a degree of 2 (2 branches)
    - If a single node has no children, it is a perfect binary tree of height h = 0
    - If a node has h > 0, it is a perfect binary tree if both of its subtrees are of height h - 1 and are non-overlapping

* [Complete Binary Tree](/Practice%20Concepts/Trees/complete-binary-tree.py): 
    - All levels are completely filled except possibly the lowest one, which is filled from the left.
    - Similar to full binary trees except - 
        1. All the leaf elements must lean towards the left.
        2. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/cb1.png)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/cb2.png)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/cb3.png)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/cb4.png)

    ![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/cb5.png)

    - We can use this tree to find the children and parent of any node

* Degenerate / Pathological Tree - A tree having a single child either left or right

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/dgen.png)

* Skewed Binary Tree - A pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/skew.png)

* [Balanced Binary Tree](/Practice%20Concepts/Trees/complete-binary-tree.py):
    - Binary tree in which the height of the left and right subtree of any node differ by not more than 1.
        - difference between the left and the right subtree for any node is not more than one
        - the left subtree is balanced
        - the right subtree is balanced


### [Binary Search Tree](/Practice%20Concepts/Trees/binary-search-tree.py)
* Quickly allows us to maintain a sorted list of numbers
* It has a maximum of 2 child nodes and can search for a number in O(log(n)) time.
* How is binary search tree different from a binary tree - 
    1. All nodes on the left subtree are lesser than the root node
    2. All nodes on the right subtree are greater than the root node
    3. Both subtrees of each node are also BSTs

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/bst.png)

* The binary tree on the right isn't a binary search tree because the right subtree of the node "3" contains a value smaller than it.
* Operations:
    - SEARCH: If the value is below the root, we can say for sure that the value is not in the right subtree; we need to only search in the left subtree and if the value is above the root, we can say for sure that the value is not in the left subtree; we need to only search in the right subtree. If the value is found in any of the subtrees, it is propagated up so that in the end it is returned, otherwise null is returned.
    - INSERT: Inserting a value in the correct position is similar to searching. We keep going to either right subtree or left subtree depending on the value and when we reach a point left or right subtree is null, we put the new node there.
    - DELETION:
        - CASE 1: The node to be deleted is the leaf node - simply delete the node from the tree
        - CASE 2: The node to be deleted has a single child node - replace that node with its child node, remove the child node from its original position
        - CASE 3: The node to be deleted has two children - get the inorder successor of that node, replace the node with the inorder successor, remove the inorder successor from its original position
* Best Case Time Complexity: O(log(n))
* Worst Case Time Complexity: O(n)
* Space Complexity: O(n)

### [AVL Tree](/Practice%20Concepts/Trees/binary-search-tree.py)
* TODO

### [B Tree](/Practice%20Concepts/Trees/binary-search-tree.py)
* TODO

### [Red Black Tree](/Practice%20Concepts/Trees/binary-search-tree.py)
* TODO

## Graphs
<p align="center">
    <a href="#graph-basics">Graph Basics</a> •
    <a href="#spanning-tree">Spanning Tree</a> •
    <a href="#strongly-connected-components">Strongly Connected Components</a> •
    <a href="#adjacency-matrix">Adjacency Matrix</a> •
    <a href="#adjacency-list">Adjacency List</a> •
    <a href="#dfs-algorithm">DFS Algorithm</a> •
    <a href="#breadth-first-search">Breadth First Search</a> •
    <a href="#bellman-fords-algorithm">Bellman Ford's Algorithm</a>
</p>

### Graph Basics
* A collection of nodes that have data and are connected to other nodes. 
* A graph is a data structure (V, E) - collection of vertices V, a collection of edges E [represented as ordered pairs of vertices (u,v)]

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/graph.png)

* V = {0, 1, 2, 3} | E = {(0,1), (0,2), (0,3), (1,2)} | G = {V, E}
* Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them. Vertices 2 and 3 are not adjacent because there is no edge between them.
* Path: A sequence of edges that allows you to go from vertex A to vertex B. 0-1, 1-2 and 0-2 are paths from vertex 0 to vertex 2.
* Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well. The edges in such a graph are represented by arrows to show the direction of the edge.
* Graph Representations: Adjacency Matrix and Adjacency List

### Spanning Tree
* Undirected Graph: Graph in which the edges do not point in any direction - bidirectional
* Connected Graph: Graph in which there is always a path from a vertex to any other vertex
* Spanning Tree: Sub-graph of an undirected connected graph, which includes all the vertices of the graph with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree.
* The total number of spanning trees with n vertices that can be created from a complete graph is equal to n<sup>(n-2)</sup>
* A minimum spanning tree is a spanning tree in which the sum of the weight of the edges is as minimum as possible.

### [Strongly Connected Components](/Practice%20Concepts/Graphs/scc.py)
* Portion of a directed graph in which there is a path from each vertex to another vertex - applicable only on a directed graph.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/strongly-connected.png)

* Kosaraju's Algorithm:
    - Based on depth-first search algorithm, implemented twice
    1. Create an empty stack and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, push the vertex to stack.
    2. Reverse the direction of all arcs to obtain the transposed graph
    3. One by one pop a vertex from the stack. Perform DFS on this, which prints SCC.

### [Adjacency Matrix](/Practice%20Concepts/Graphs/adj-mat.py)
* Representing graphs as a matrix of 0s and 1s - boolean value of the matrix indicates if there is a direct path between two vertices.
* Each cell in the matrix is represented as A(i,j) where i and j are vertices.
* The value of A(i,j) is either 1 or 0 depending on whether there is an edge from vertex i to vertex j.
* In case of undirected graphs, the matrix is symmetric about the diagonal because of every edge (i,j), there is also an edge (j,i).
* Advantages - 
    1. Basic operations are time efficient - constant time operations
    2. Even if the graph and the adjacency matrix is sparse, we can represent it using data structures for sparse matrices.
    3. By performing operations on the adjacent matrix, we can get important insights into the nature of the graph and the relationship between its vertices.
* Disadvantages - 
    1. The VxV space requirement of the adjacency matrix makes it a memory hog. 
    2. Operations like inEdges and outEdges are expensive when using the adjacency matrix representation.

### [Adjacency List](/Practice%20Concepts/Graphs/adj-list.py)
* Represents a graph as an array of linked lists. The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.
* Advantages - 
    1. Efficient in terms of storage because we only need to store the values for the edges. 
    2. It also helps to find all the vertices adjacent to a vertex easily.
* Disadvantages - 
    1. Finding the adjacent list is not quicker than the adjacency matrix because all the connected nodes must be first explored to find them.

### [DFS Algorithm](/Practice%20Concepts/Graphs/dfs.py)
* Recursive algorithm for searching all the vertices of a graph or tree.
* Vertex categorized as visited or not visited
* The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.
* Working of DFS - 
    1. Place any vertex on top of a stack
    2. Take top item of the stack and add it to the visited list
    3. Create a list of that vertex's adjacent nodes - Add the ones which aren't in the visited list to the top of the stack.
    4. Keep repeating 2 and 3 until stack is empty
* Time complexity - O(V + E), where V is the number of nodes and E is the number of edges.
* Space complexity - O(V).

### [Breadth First Search](/Practice%20Concepts/Graphs/bfs.py)
* Recursive algorithm for searching all the vertices of a graph or tree data structure.
* The algorithm works as follows:
    1. Start by putting any one of the graph's vertices at the back of a queue.
    2. Take the front item of the queue and add it to the visited list
    3. Create a list of that vertex's adjacent nodes - add the ones which aren't in the visited list to the back of the queue.
    4. Keep repeating steps 2 and 3 until the queue is empty.

* The graph might have two different disconnected parts
* Time complexity - O(V + E), where V is the number of nodes and E is the number of edges.
* Space complexity - O(V).


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
<p align="center">
    <a href="#bubble-sort">Bubble Sort</a> •
    <a href="#selection-sort">Selection Sort</a> •
    <a href="#insertion-sort">Insertion Sort</a> •
    <a href="#merge-sort">Merge Sort</a> •
    <a href="#quick-sort">Quick Sort</a> •
    <a href="#counting-sort">Counting Sort</a> •
    <a href="#radix-sort">Radix Sort</a> •
    <a href="#bucket-sort">Bucket Sort</a> •
    <a href="#heap-sort">Heap Sort</a> •
    <a href="#shell-sort">Shell Sort</a>
</p>

### [Bubble Sort](/Practice%20Concepts/Sorting/bubble-sort.py) 
* Bubble Sort will sort by checking if the next element is greater than the present element - if greater then it will swap the elements.
* Use of 2 loops - outer and inner 
* Each element is compared to its adjacent element - if current is greater, then we swap them
* At the end of the first iteration, the largest element will be at the end, the second largest will be at the n - 1 position
* Outer loop is to loop n times and inner loop is for swapping
* In place sorting
* Worst Case: O(n<sup>2</sup>)
* Best Case: O(1) - because an extra variable is used for swapping.

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Bubble-sort.gif)

### [Selection Sort](/Practice%20Concepts/Sorting/selection-sort.py) 
* Selection Sort is a sorting technique where the smallest element is taken from the array and placed at the first index - this is repeated for the remaining elements. 
* Get the smallest element from the array, exchange it with the first index element
* Second smallest element swap with second index position, and so forth 
* Need of 2 loops - outer loop iterate all the array elements one by one, inner loop - here the element from the outer loop is checked against all the elements from inner loop. If a smaller element is found, then that element will be replaced with the index of outer loop
* Best, Worst Case: O(n<sup>2</sup>)
* Space Complexity: O(1)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Selection-Sort.gif)

### [Insertion Sort](/Practice%20Concepts/Sorting/insertion-sort.py) 
* Insertion Sort is an efficient algorithm for sorting a small number of elements.
* In-place sorting - rearranges the elements in place.
* Keys: Numbers that we wish to sort
* Divide array into sorted and unsorted elements, select first unsorted element (key), swap the sorted elements to the right to create the correct position and shift the unsorted element (key), advance marker to right (next key)
* Best Case: O(n)
* Worst Case: O(n<sup>2</sup>)
* Space Complexity: O(1)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Insertion-Sort.gif)

### [Merge Sort](/Practice%20Concepts/Sorting/merge-sort.py)
* Based on the divide and conquer strategy
* Divide: Divide the array into half, and continue to do so with the resultant arrays until only single elements are left
* Conquer: Sort the left part and right part of the array recursively
* Combine: Combine the left and right arrays to form one complete, sorted array
* External Sorting, Stable
* Best Case, Worst Case and Average Case: O(nlogn)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/Merge-Sort.gif)

### [Quick Sort](/Practice%20Concepts/Sorting/quick-sort.py)
* Based on the Divide and Conquer strategy
* Method:
    1. Select the pivot element: Different variations have different methods of picking the pivot elements. The most basic one picks the right-most element as the pivot element. 
    2. Rearrange the array: Arranged in the manner so that the elements smaller than the pivot are to the left whereas the elements larger than the pivot are stored on the right. 
        - Pointer fixed at the pivot element. This is compared with the element starting from the first index
        - Second pointer set for the element if it is larger than the pivot
        - Pivot is compared with other elements - If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier.
        - Process is repeated to set the next greater element as the second pointer. And, swap it with another smaller element.
        - The process goes on until the second last element is reached
        - Pivot swapped with the new second pointer.
    3. Divide the subarrays - Pivot elements are again chosen for the left and the right sub-parts separately. And, step 2 is repeated. The subarrays are divided until each subarray is formed of a single element.
* Time complexity: 
    - Best, Average: O(nlog(n))
    - Worst: O(n<sup>2</sup>)
* Space Complexity: O(log(n))

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/quicksort.gif)

### [Counting Sort](/Practice%20Concepts/Sorting/counting-sort.py)
* Sorts the elements of an array by counting the number of occurances of each unique element in the array.
* The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.
* Method:
    - Find out the maximum element
    - Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array.
    - Store the count of each element at their respective index in the 'count' array
    - Store cumulative sum of the elements of the count array. It helps in placing the elements into the correct index of the sorted array.
    - Find the index of each element of the original array in the count array. This gives the cumulative count. 
    - After placing each element at its correct position, decrease its count by one
* Time Complexity - Best, Average and Worst: O(n + k) - There are mainly four main loops
* Space Complexity - O(max)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/counting-sort.gif)

### [Radix Sort](/Practice%20Concepts/Sorting/radix-sort.py)
* Sorts the elements by first grouping the individual digits of the same place value. Then, sort the elements according to their increasing/decreasing order.
* Method:
    - Find the largest element in the array
    - Find the number of digits of the largest element - calculated because we have to go through all the significant places of all elements.
    - Go through each significant place one by one
* Time Complexity - Best, Average and Worst: O(n + k) 
* Space Complexity - O(max)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/radix-sort.gif)

### [Bucket Sort](/Practice%20Concepts/Sorting/bucket-sort.py)
* Sorting algorithm that divides the unsorted array elements into several groups (buckets)
* Each bucket is then sorted by using any of the suitable sorting algorithms or recursively applying the same bucket algorithm
* Method:
    - Create an array of size n. Each slot of this array is used as a bucket for storing elements.
    - Insert elements into the buckets from the array. The elements are inserted according to the range of the bucket.
    - The elements of each bucket are sorted using any of the stable sorting algorithms
    - The elements from each bucket are gathered
* Time Complexity: 
    - Best: O(n + k)
    - Average: O(n)
    - Worst: O(n<sup>2</sup>) 
* Space Complexity - O(n + k)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/bucket.webp)

### [Heap Sort](/Practice%20Concepts/Sorting/heap-sort.py)
* Heap sort works by visualizing the elements of the array as a special kind of complete binary tree called a heap.
* If the index of any element in the array is i, the element in the index 2i+1 will become the left child and element in 2i+2 index will become the right child. Also, the parent of any element at index i is given by the lower bound of (i-1)/2
* A binary tree is said to follow a heap data structure if - it is a complete binary tree and all nodes in the tree follow the property that they are greater than their children - the largest element is at the root and both its children and smaller than the root and so on. Such a heap is called a max-heap. If instead, all nodes are smaller than their children, it is called a min-heap

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/min-max-heap.png)

* Starting from a complete binary tree, we can modify it to become a Max-Heap by running a function called heapify on all the non-leaf elements of the heap.
* To maintain the max-heap property in a tree where both sub-trees are max-heaps, we need to run heapify on the root element repeatedly until it is larger than its children or it becomes a leaf node.
* Heap Sort Method:
    - Since the tree satisfies Max-Heap property, then the largest item is stored at the root node.
    - Swap: Remove the root element and put at the end of the array (nth position) Put the last item of the tree (heap) at the vacant place
    - Remove: Reduce the size of the heap by 1
    - Heapify: Heapify the root element again so that we have the highest element at root
    - Repeat this process
* Time Complexity - O(nlog(n)) 
* Space Complexity - O(1)

![](https://github.com/aish21/Algorithms-and-Data-Structures/blob/main/Resources/Animations/heapsort.gif)

## Search Algorithms
<p align="center">
    <a href="#linear-search">Linear Search</a> •
    <a href="#binary-search">Binary Search</a>
</p>

## Greedy Algorithms
<p align="center">
    <a href="#introduction-to-greedy-algorithms">Introduction to Greedy Algorithms</a> •
    <a href="#ford-fulkerson-algorithm">Ford Fulkerson Algorithm</a> •
    <a href="#dijkstra-algorithm">Dijkstra Algorithm</a> •
    <a href="#kruskal-algorithm">Kruskal Algorithm</a> •
    <a href="#prim-algorithm">Prim Algorithm</a> •
    <a href="#huffman-coding">Huffman Coding</a>
</p>

## Dynamic Programming
<p align="center">
    <a href="#introduction-to-dynamic-progamming">Introduction to Dynamic Programming</a> •
    <a href="#floyd-warshall-algorithm">Floyd Warshall Algorithm</a> •
    <a href="#longest-common-sequence">Longest Common Sequence</a>
</p>

## Other Algorithms
<p align="center">
    <a href="#backtracking-algorithm">Backtracking Algorithm</a> •
    <a href="#rabin-karp-algorithm">Rabin Karp Algorithm</a>
</p>

## Leetcode Explanation
<p align="center">
    <a href="#easy-problems">Easy Problems</a> •
    <a href="#medium-problems">Medium Problems</a> •
    <a href="#hard-problems">Hard Problems</a>
</p>

### [Easy Problems](/Leetcode%20Problems/Easy)
* [13 - Roman to Integer](/Leetcode%20Problems/Easy/13-Roman-to-Integer.py)
    - Concepts: Strings, Maps
    - Need to create a dictionary to map the symbols to the values
    - Move from right to left of the given string
    - If the value is greater, add to the result (I + I = 2)
    - If the value is lesser, subtract (for IV = 4)

### [Medium Problems](/Leetcode%20Problems/Medium)
* [1249 - Minimum Remove to Make Valid Parentheses](/Leetcode%20Problems/Medium/1249-Minimum-Remove-to-Make-Valid-Parentheses.py)
    - Concepts: Strings, Stacks
    - Create a stack to keep note of initial paranthesis - (
    - If ) is found and stack is empty, add the index to the set for indexes to be removed, else pop the index in stack (since we have a valid parenthesis)
    - Combine the index to be removed set and the indexes stored in the stack
    - Result is all the values except the combined index values
    
### [Hard Problems](/Leetcode%20Problems/Hard)
* []
