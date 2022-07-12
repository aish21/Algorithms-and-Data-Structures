import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        ans = math.log(n, 3)
        return math.fabs(ans - round(ans)) < 0.0000000001