class Queue:
    def __init__(self) -> None:
        self.currSize = 0
        self.maxSize = 10
        self.arr = [0] * self.maxSize
        self.front = -1
        self.rear = -1

    def push(self, val) -> None:
        if self.currSize == self.maxSize:
            print("The queue is full")
            exit(1)
        if self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear+1) % self.maxSize
        self.arr[self.rear] = val
        self.currSize += 1
        

    def pop(self)->int:
        if self.front == -1:
            print("The queue is empty")
            exit(1)
        val = self.arr[self.front]
        if self.currSize == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.maxSize
        self.currSize -= 1
        return val
    
    def top(self) -> int:
        if self.front == -1:
            print("The queue is empty")
            exit(1)
        return self.arr[self.front]
    
    def size(self):
        return self.currSize
    
q = Queue()
q.push(4)
q.push(14)
q.push(24)
q.push(34)
print("The peek of the queue before deleting any element", q.top())
print("The size of the queue before deletion", q.size())
print("The first element to be deleted", q.pop())
print("The peek of the queue after deleting an element", q.top())
print("The size of the queue after deleting an element", q.size())


