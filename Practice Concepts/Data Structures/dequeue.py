from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def enqueue_front(self, item):
        self.deque.appendleft(item)  # Add item to the front

    def enqueue_rear(self, item):
        self.deque.append(item)  # Add item to the rear

    def dequeue_front(self):
        if not self.is_empty():
            return self.deque.popleft()  # Remove and return the front item
        raise IndexError("Dequeue from an empty deque")

    def dequeue_rear(self):
        if not self.is_empty():
            return self.deque.pop()  # Remove and return the rear item
        raise IndexError("Dequeue from an empty deque")

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

# Test cases
deque = Deque()
deque.enqueue_front(10)
deque.enqueue_front(20)
deque.enqueue_rear(30)
assert deque.dequeue_front() == 20
assert deque.dequeue_rear() == 30
assert deque.size() == 1
assert deque.is_empty() == False
assert deque.dequeue_front() == 10
assert deque.is_empty() == True
assert deque.size() == 0
