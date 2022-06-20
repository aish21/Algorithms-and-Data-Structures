<h1 align="center">
  <br>
  Algorithms and Data Structure: A Comprehensive Guide
  <br>
</h1>

<h4 align="center">My notes on concepts covering algorithms and data structures</h4>

<p align="center">
  <a href="#Introduction">Introduction to Algorithms (Complexity Analysis)</a> •
  <a href="#Sorting">Sorting Algorithms</a> •
  <a href="#Searching">Search Algorithms</a> •
  <a href="#Data-Structures">Introduction to Data Structures</a> •
  <a href="#Trees">Trees</a> •
  <a href="#Graphs">Graphs</a> •
</p>

## Introduction to Algorithms (Complexity Analysis)
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
