class Stack:
    def __init__(self) -> None:
        self.top = -1
        self.size = 10
        self.arr = [0] * self.size
        

    def push(self, val):
        if self.top == self.size:
            print("The stack is full")
            return
         
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            print("The stack is empty")
            return
        
        val = self.arr[self.top]
        self.top -= 1
        return val
    
    def Top(self):
        return self.arr[self.top]
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def Size(self):
        return self.top + 1
        

s = Stack()
s.push(6)
s.push(3)
s.push(7)
print("Top of stack is before deleting any element", s.Top())
print("Size of stack before deleting any element", s.Size())
print("The element deleted is", s.pop())
print("Size of stack after deleting an element", s.Size())
print("Top of stack after deleting an element", s.Top())