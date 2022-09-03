'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
'''

class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.movingAvg = 0
        self.size = size
        self.count = 0
        self.total = 0

    def next(self, val: int) -> float:
        if(len(self.queue) < self.size):
            self.queue.append(val)
            self.count += 1
            self.total += val
            self.movingAvg = (self.total) / self.count
            return self.movingAvg
        
        else:
            self.total -= self.queue[0]
            self.queue.pop(0)
            self.queue.append(val)
            self.total += val
            self.movingAvg = (self.total) / self.size
            return self.movingAvg
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)