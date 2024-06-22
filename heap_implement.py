import math


class Node:
    def __init__(self, val, left = None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Heap:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(self.arr)
        for i in range(self.n-1, -1, -1):
            self.heapify(i, self.n)

    # max-heap
    def heapify(self, i, n):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left > n and right > n:
            return
        if i < n and left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if i < n and right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest, n)

    def shiftUp(self, index):
        parentIndex = (index-1)//2
        while index > 0 and self.arr[index] > self.arr[parentIndex]:
            self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
            index = parentIndex
            parentIndex = (index-1) // 2
        

    def insert(self, val):
        self.arr.append(val)
        self.shiftUp(len(self.arr)-1)

    def top(self):
        return self.arr[0]
    
    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop(len(self.arr)-1)
        self.heapify(0, len(self.arr))


arr = [12, 11, 13, 5, 6, 7]
heap = Heap(arr)
print(heap.arr)

heap.insert(15)
print(heap.arr)

print(heap.top())

heap.pop()
print(heap.arr)
      


   