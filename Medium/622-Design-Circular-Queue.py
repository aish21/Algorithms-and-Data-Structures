class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.size = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if(self.count == self.size):
            return False
        self.queue[(self.head + self.count) % self.size] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if(self.count == 0):
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if(self.count == 0):
            return -1
        return self.queue[self.head]
        

    def Rear(self):
        """
        :rtype: int
        """
        if(self.count == 0):
            return -1
        return self.queue[(self.head + self.count - 1) % self.size]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()