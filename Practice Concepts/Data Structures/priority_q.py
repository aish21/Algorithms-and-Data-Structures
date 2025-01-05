import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        heapq.heappush(self.queue, item)  # Push item while maintaining heap order

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)  # Remove and return the smallest item
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Front from an empty queue")
    
    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        raise IndexError("Rear from an empty queue")

# Test Cases
queue = PriorityQueue()
queue.enqueue(30)
queue.enqueue(10)
queue.enqueue(20)
assert queue.front() == 10
assert queue.rear() == 20
assert queue.dequeue() == 10
assert queue.front() == 20
assert queue.rear() == 30
assert queue.dequeue() == 20
assert queue.front() == 30
assert queue.rear() == 30
assert queue.dequeue() == 30
assert queue.is_empty() == True
