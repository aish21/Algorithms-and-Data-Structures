'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        # Time Limit Exceeded
        output = ''
        for i in range(len(s)):
            temp = ''
            for letter in s:
                temp = temp + letter
                if(temp == temp[::-1]):
                    if(len(temp) > len(output)):
                        output = temp
            s = list(s)
            s.pop(0)
            s = ''.join(s)
            print(s)
        
        return output
        '''
        
        longest = ''
        def findLongest(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            s1 = findLongest(s, i, i)
            if len(s1) > len(longest): longest = s1
            
            s2 = findLongest(s, i, i+1)
            if len(s2) > len(longest): longest = s2
                
        return longest