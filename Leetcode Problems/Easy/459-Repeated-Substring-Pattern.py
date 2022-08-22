'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            if len(s) % i == 0:
                if all(s[j]==s[j-i] for j in range(i, len(s))):
                    return True
        
        return False