'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        output = []
        current = head
        while current is not None:
            output.append(current.val)
            current = current.next
        return output == output[::-1]