# Basics - Introduction
###### This section covers the basic, underlying concepts of algorithms and data structure, to provide a solid foundation for more complex cases and problems in this domain. 

- **Variables** are placeholders for data (in equations and programming logic)
- These variables take the form of specific data types. **Data types** are a set of data with predefined values - integers, floats, characters, string, boolean, etc
- Data types occupy a set amount of memory units (bytes). There are two types of data types - primitive (system defined) and user defined data types.
- **Primitive data types** - char, int, float, double, bool, etc - provided by the programming language - the number of bits allocated to each data type depends on the programming language, compiler and the operating system. 
- **User defined data types** - structures in C and classes in Java - when primitive data types are not enough - gives more flexibility, we can combine primitive types.
- **Data structure** is a way of storing and organising data in a computer - arrays, linked lists, stacks, queues, trees, graphs
- **Linear data structures** - elements accessed in sequential order, but not necessarily stored that way - linked lists, stacks and queues.
- **Non Linear data structures** - elements stored and accessed in a non-linear order - trees and graphs
- **Abstract Data Types** - When we combine data structures with their operations, which involves the declaration of data and operations. 
- An **algorithm** is the step by step instructions to solve a given problem. There are multiple algorithms to solve the same problem, and the analysis of these algorithms helps determine the algorithms most efficient in terms of computation time and space consumed. 
- The goal of algorithmic analysis is to compare different algorithms in terms of **running time** and **memory**. 
- Running time analysis involves determining the increase in processing time as the size of input (number of elements) increases.
- Algorithms are compared by expressing the running time of a given algorithm as a function of the input - independent of factors such as machine capability, programming style.
- Rate of growth is defined as the rate at which the running time increases (with input)
- **Rates of growth** - 
``` n! > 4^n  > 2^n  > n^2  > nlog(n) > log(n!) > n > 2^logn  > log^2(n) > sqrt(logn) > log(logn) > 1 ```
- **Worst Case**: Defines the input for which the algorithm takes the longest time (slowest)
- **Best Case**: Defines the input for which the algorithm takes the least time (fastest)
- **Average Case**: Provides a prediction about the running of the algorithm - random input
- Upper and lower bounds need to be computed for all the 3 aforementioned cases - need notations to represent these bounds.
- **Big-O Notation** - Gives the tight upper bound for a function. Outputs a function which gives the maximum rate of growth for the input function at larger values of n (input). We usually consider values of input above a given threshold. 
- **Omega Notation**: Gives the tight lower bound for a given algorithm. 
- **Theta Notation**: Decides whether the upper and lower bounds are the same for a given algorithm. In this case, best case and worst case are the same - average case will also be the same.
- The general focus is on the upper bound of an algorithm - Big-O Notation.
- **Loops:** The running time of a loop is, at most, the running time of the statements inside the loop (including tests) multiplied by the number of iterations
- **Nested Loops:** Analyse from the inside out. Total running time is the product of the sizes of all the loops
- **Consecutive Statements:** Add the time complexities of each statement
- **If-then-else statements:**  Worst case running time: the test, plus either the *then* part or the *else* part (whichever is the larger)
- **Logarithmic complexity:** An algorithm is O(logn) if it takes a constant time to cut the problem size by a fraction
- More information + mathematical induction can be found in the [Basics](/Basics) directory (images).
