'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        combList = []
        for i in range(len(s)):
            temp = list(s)
            temp.pop(i)
            temp = ''.join(temp)
            combList.append(temp)
        
        for i in range(len(combList)):
            if(combList[i] == combList[i][::-1]):
                return True
        return False
        '''
        i = 0
        j = len(s) - 1
        
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.helper(s, i + 1, j) or self.helper(s, i, j - 1)

                
        return True
    
    def helper(self, s, left, right):
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
        '''    