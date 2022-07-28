'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indexRemove = set()
        i = 0
        result = ''
        
        for c in s:
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    indexRemove.add(i)
                else:
                    stack.pop()
            i += 1
        
        indexRemove = indexRemove.union(stack)
        for i in range(len(s)):
            if i not in indexRemove:
                result += s[i]
        
        return result