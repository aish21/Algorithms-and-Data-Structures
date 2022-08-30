'''
You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.
'''

class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            if c[str(i)] == int(num[i]):
                continue
            else:
                return False
        return True