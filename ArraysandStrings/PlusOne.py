'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''

def plusOne(self, digits: List[int]) -> List[int]:
    res = []
    digits = [str(i) for i in digits]
    val = ''.join(digits)
    val = int(val)
    val += 1
    res = [int(i) for i in str(val)]
    return res