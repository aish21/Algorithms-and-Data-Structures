# Python implementation of a simple queue

from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.popleft() # Remove and return the first element
        raise IndexError('Queue is empty')
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def front(self):
        if not self.isEmpty():
            return self.queue[0] # Return the FRONT of the queue without removing it
        raise IndexError('Queue is empty')
    
    def rear(self):
        if not self.isEmpty():
            return self.queue[-1] # Return the REAR of the queue without removing it
        raise IndexError('Queue is empty')

# Test Cases
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
assert queue.front() == 1
assert queue.rear() == 3
assert queue.dequeue() == 1
assert queue.front() == 2
assert queue.rear() == 3
assert queue.dequeue() == 2
assert queue.front() == 3
assert queue.rear() == 3
assert queue.dequeue() == 3
assert queue.isEmpty() == True
