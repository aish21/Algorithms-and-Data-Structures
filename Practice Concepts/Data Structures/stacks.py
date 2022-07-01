# Python implementation of stacks 

# Create a Stack
def create_stack():
    stack = []
    return stack

# Check if the stack is empty
def IsEmpty(stack):
    return len(stack) == 0

# PUSH operation
def PUSH(stack, value):
    stack.append(value)
    print('Pushed - ' + value)

# POP operation
def POP(stack):
    if(IsEmpty(stack)):
        return "Stack is empty"
    return stack.pop()

# Driver code
stack = create_stack()
print("Empty Stack - " + str(stack))
PUSH(stack, str(1))
PUSH(stack, str(10))
PUSH(stack, str(100))
PUSH(stack, str(1000))
print("After PUSH - " + str(stack))
print("Popped - " + POP(stack))
print('Resultant Stack - ' + str(stack))