'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Solution is in O(n) time complexity. Accepting suggestions on how to make it in O(1) complexity

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        outputList = []
        s = s.split(' ')
        print(s)
        for word in s[::-1]:
            if word == '':
                continue
            else:
                outputList.append(word)
        output = ' '.join(outputList)
        return output
            
