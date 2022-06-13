class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        expected = sorted(heights)
        
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                ans += 1
        return ans