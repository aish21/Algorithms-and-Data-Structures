class Solution:
    def reverseWords(self, s: str) -> str:
        sep = s.split()
        ans = []
        for word in sep:
            ans.append(word[::-1])
        
        return " ".join(ans)