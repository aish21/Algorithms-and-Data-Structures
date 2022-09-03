'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        sDic = Counter(s)
        for i in range(len(s)):
            if sDic[s[i]] == 1:
                return i
        return -1 
        