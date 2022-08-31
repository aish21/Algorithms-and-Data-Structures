'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if((i % 3 == 0) and (i % 5 == 0)):
                answer.append("FizzBuzz")
                continue
            elif(i % 3 == 0):
                answer.append("Fizz")
                continue
            elif(i % 5 == 0):
                answer.append("Buzz")
                continue
            else:
                answer.append(str(i))
        return answer
            