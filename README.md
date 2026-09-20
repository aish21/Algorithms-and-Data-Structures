# Algorithms & Data Structures

Active interview-preparation notes, implementations, and solved problems in Python.

I originally created this repository as a broad DSA reference. I am now using it as a structured interview-prep workspace: focusing on recurring problem-solving patterns, the reasoning behind them, complexity analysis, and clean implementations.

## Active interview prep

Start here:

**[Interview Prep](interview-prep/README.md)**

Current focus:

- Arrays — complete
- Hash maps & sets — complete
- Two pointers — in progress
- Sliding window — next

The newer notes are organised around interview patterns rather than around isolated LeetCode problems.

## Repository structure

```text
interview-prep/
  README.md
  patterns/
    two-pointers.md

Practice Concepts/
  Data Structures/
  Trees/
  Graphs/
  Greedy Algorithms/
  Dynamic Programming/
  ...

Leetcode Problems/
  Easy/
  Medium/
  Hard/

archive/
  legacy-notes.md
```

## Selected problems

A few useful examples already in the repository:

- [Two Sum — hash map](Leetcode%20Problems/Easy/1-Two-Sum.py)
- [Two Sum II — two pointers](Leetcode%20Problems/Easy/167-Two-Sum-II-Input-Array-Is-Sorted.py)
- [Valid Palindrome](Leetcode%20Problems/Easy/125-Valid-Palindrome.py)
- [LRU Cache](Leetcode%20Problems/Medium/146-LRU-Cache.py)
- [Minimum Remove to Make Valid Parentheses](Leetcode%20Problems/Medium/1249-Minimum-Remove-to-Make-Valid-Parentheses.py)

## Study philosophy

For interview preparation I care about being able to explain:

1. what signal in the problem suggests a pattern;
2. what invariant/state the algorithm maintains;
3. why each decision is safe;
4. the time and space complexity;
5. the edge cases and common failure modes.

The aim is understanding and recall under interview conditions, not simply accumulating solved problems.

## Historical notes

The repository's original long-form reference notes are preserved here:

**[Legacy DSA notes](archive/legacy-notes.md)**
