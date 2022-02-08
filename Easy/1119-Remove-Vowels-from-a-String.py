'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
'''

class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = ""
        
        for ch in s:
            if ch not in ('a', 'e', 'i', 'o', 'u'):
                final += ch
        
        return final