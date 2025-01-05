# Python implementation of Circular Q

class CircularQ():

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0 
        self.rear = -1
        self.size = 0
    
    def enqueue(self, value):
        if self.size == self.capacity:
            raise OverflowError('Queue is full')
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue is empty')
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def isEmpty(self):
        return self.size == 0
    
    def front(self):
        if not self.isEmpty():
            return self.queue[self.front]
        raise IndexError('Queue is empty')
    
    def rear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        raise IndexError('Queue is empty')

# Test Cases
queue = CircularQ(3)
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