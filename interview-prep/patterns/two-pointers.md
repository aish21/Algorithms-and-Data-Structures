# Two Pointers

## Core idea

Two pointers maintain two positions in a sequence and move them according to information from the current state.

The important idea is not simply "use two indices." Each pointer movement should let us safely eliminate possibilities.

## 1. Opposite-end pointers

Typical setup:

```python
left = 0
right = len(nums) - 1

while left < right:
    ...
```

Common triggers:

- sorted array + pair/target;
- palindrome checks;
- reversing;
- shrinking a search interval.

### Sorted pair sum

For a sorted array:

```text
[1, 3, 4, 6, 8, 10]
 ^               ^
 L               R
```

Let:

```python
current = nums[left] + nums[right]
```

Decision rule:

- if `current < target`, move `left` right;
- if `current > target`, move `right` left;
- if `current == target`, the pair is found.

Why this works:

- when the sum is too small, moving the right pointer left can only make the sum smaller, so the left pointer must move;
- when the sum is too large, moving the left pointer right can only make the sum larger, so the right pointer must move.

The sorted order is what makes these eliminations safe.

### Complexity

Each pointer moves in only one direction and crosses the array at most once:

- Time: **O(n)**
- Extra space: **O(1)**

### Existing example

- [LeetCode 167 — Two Sum II](../../Leetcode%20Problems/Easy/167-Two-Sum-II-Input-Array-Is-Sorted.py)

## 2. Palindrome pattern

Compare the outer characters and move inward:

```python
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1

return True
```

This is O(n) time and O(1) extra space if the input does not need to be copied or normalised first.

A previous solution in this repository checks a cleaned string using slicing:

- [LeetCode 125 — Valid Palindrome](../../Leetcode%20Problems/Easy/125-Valid-Palindrome.py)

A later revision can implement the full two-pointer version directly on the original string.

## 3. Same-direction pointers

The pointers may also move in the same direction.

Typical roles:

- `fast`: scans/explores;
- `slow`: tracks the next valid position or the boundary of a region.

Common uses:

- remove duplicates in-place;
- compact arrays;
- partition values;
- subsequence checks.

Example shape:

```text
[1, 1, 2, 2, 3]
 ^     ^
slow  fast
```

## When to consider two pointers

Think about this pattern when the problem contains one or more of:

- sorted input;
- pair or target-sum reasoning;
- comparison from both ends;
- in-place compaction;
- a left/right boundary that changes monotonically.

## Two pointers vs hash map

For unsorted Two Sum:

- hash map: O(n) time, O(n) space.

For sorted Two Sum:

- two pointers: O(n) time, O(1) extra space.

Sorting an unsorted array first gives O(n log n) overall and may lose the original-index information, so it is not automatically better.

## Common mistakes

- Using two pointers on unsorted data without another invariant that justifies movement.
- Moving the wrong pointer when the sum is too small or too large.
- Using `left <= right` for a pair problem and accidentally allowing the same element twice.
- Memorising pointer movement without being able to explain why discarded candidates cannot work.

## Mental model

**Current state -> compare -> eliminate impossible region -> move one pointer.**

The algorithm is efficient because every move permanently rules something out.
