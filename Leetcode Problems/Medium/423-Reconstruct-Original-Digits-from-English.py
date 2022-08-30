'''
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
'''

class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        
        res = [0] * 10
        
        res[0] = c['z']
        res[2] = c['w']
        res[4] = c['u']
        res[6] = c['x']
        res[8] = c['g']
        res[1] = c['o'] - res[0] - res[2] - res[4]
        res[3] = c['h'] - res[8]
        res[5] = c['f'] - res[4]
        res[7] = c['s'] - res[6]
        res[9] = c['i'] - res[5] - res[6] - res[8]
        
        output = []
        
        for i in range(10):
            output.append(str(i) * res[i])
        
        return "".join(output)