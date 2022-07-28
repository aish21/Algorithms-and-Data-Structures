'''
Given a roman numeral, convert it to an integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Map the symbols to the integer values
        symbolMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        strLen = len(s)
        
        result = symbolMap[s[strLen - 1]]
        
        # Move from right to left
        for i in range(strLen - 2, -1, -1):
            
            if(symbolMap[s[i]] >= symbolMap[s[i + 1]]):
                result += symbolMap[s[i]]
            else:
                result -= symbolMap[s[i]]
        
        return result