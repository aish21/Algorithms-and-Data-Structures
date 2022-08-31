'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = 0
        a = 0
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit() and abbr[a] != '0':
                e = a
                while e < len(abbr) and abbr[e].isdigit(): 
                    e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            else:
                if word[w] != abbr[a]:
                    return False
                w += 1
                a += 1
        return w == len(word) and a == len(abbr)