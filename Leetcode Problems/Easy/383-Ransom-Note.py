'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
