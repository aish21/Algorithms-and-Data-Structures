'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        convInt = str(x)
        revInt = convInt[::-1]
        if(convInt == revInt):
            return True
        else:
            return False