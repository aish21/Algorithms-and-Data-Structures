'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
'''
# First solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        convInt = str(x)
        revInt = convInt[::-1]
        if(convInt == revInt):
            return True
        else:
            return False

# Second solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = x
        reverse = 0

        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        
        return x == reverse