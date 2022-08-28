'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        output = ""
        
        if strs is None or len(strs) == 0:
            return output
        
        minLength = len(strs[0])
        for i in range(1, len(strs)):
            minLength = min(minLength, len(strs[i]))
        
        for i in range(0, minLength):
            # Get the current character from the first string
            current = strs[0][i]
            
            # Check if this character is found in all other strings or not
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return output
            output += current
        return output
            
            