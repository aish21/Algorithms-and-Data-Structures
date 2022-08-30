'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while True:
            list1.append(str(l1.val))
            if(l1.next is None):
                break
            l1 = l1.next
        
        while True:
            list2.append(str(l2.val))
            if(l2.next is None):
                break
            l2 = l2.next
        
        list1 = list1[::-1]
        list2 = list2[::-1]
        num1 = int("".join(list1))
        num2 = int("".join(list2))
        
        sumOut = num1 + num2
        sumOut = list(map(int, str(sumOut)))
        sumOut = sumOut[::-1]
        
        curr = ListNode(sumOut[0])
        head = curr
        
        # iterating over output list
        for i in sumOut[1:]:
            temp = ListNode(i)
            curr.next = temp
            curr = temp

        return head