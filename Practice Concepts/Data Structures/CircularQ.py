# Python implementation of Circular Q

class CircularQ():

    def __init__(self, numElements):
        self.numElements = numElements
        self.queue = [None] * numElements
        self.FRONT = self.REAR = -1
    
    def ENQUEUE(self, value):
        if((self.REAR) + 1 % self.numElements == self.FRONT):
            print('Circular Queue is full\n')
        elif(self.FRONT == -1):
            self.FRONT = 0
            self.REAR = 0
            self.queue[self.REAR] = value
        else:
            self.REAR = (self.REAR + 1) % self.numElements
            self.queue[self.REAR] = value
    
    def DEQUEUE(self):
        if(self.FRONT == -1):
            print('Circular Queue is empty\n')
        elif(self.FRONT == self.REAR):
            temp = self.queue[self.FRONT]
            self.REAR = -1
            self.FRONT = -1
            return temp
        else:
            temp = self.queue[self.FRONT]
            self.FRONT = (self.FRONT + 1) % self.numElements
            return temp
    
    def printQ(self):
        if(self.FRONT == -1):
            print('Circular Queue is empty\n')
        elif(self.REAR >= self.FRONT):
            for i in range(self.FRONT, self.REAR + 1):
                print(self.queue[i], end = " ")
                print()
        else:
            for i in range(self.FRONT, self.numElements):
                print(self.queue[i], end = " ")
            for i in range(0, self.REAR + 1):
                print(self.queue[i], end = " ")
            print()

# Driver code
CircQ = CircularQ(5)
CircQ.ENQUEUE(1)
CircQ.ENQUEUE(2)
CircQ.ENQUEUE(3)
CircQ.ENQUEUE(4)
CircQ.ENQUEUE(5)
print("After ENQUEUE:")
CircQ.printQ()
CircQ.DEQUEUE()
print("After DEQUEUE:")
CircQ.printQ()