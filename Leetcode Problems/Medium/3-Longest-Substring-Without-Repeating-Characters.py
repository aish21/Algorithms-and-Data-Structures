'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        uniqueVal = set()
        maxLen = 0
        
        if s == "":
            return 0
        
        while end < len(s):
            if(s[end] not in uniqueVal):
                uniqueVal.add(s[end])
                end += 1
                maxLen = max(maxLen, len(uniqueVal))
            else:
                uniqueVal.remove(s[start])
                start += 1
        
        return maxLen