# Python implementation of Queues

class Queue:

    def __init__(self):
        self.queue = []
    
    # ENQUEUE
    def ENQUEUE(self, value):
        self.queue.append(value)
    
    # DEQUEUE
    def DEQUEUE(self):
        if(len(self.queue) < 1):
            return "Queue is empty"
        else:
            self.queue.pop(0)
    
    # Display
    def disp(self):
        print(self.queue)

# Driver code
q = Queue()
q.ENQUEUE(1)
q.ENQUEUE(2)
q.ENQUEUE(3)
q.ENQUEUE(4)
q.ENQUEUE(5)
print('After ENQUEUE - ')
q.disp()
q.DEQUEUE()
print('After DEQUEUE - ')
q.disp()