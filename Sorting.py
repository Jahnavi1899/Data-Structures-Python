class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge(self, p, q, r):
        arr = self.sorting_array
        nL = q-p+1
        nR = r-q
        L = []
        R = []
        for i in range (0, nL):
            L.append(arr[p+i])
        for j in range(0, nR):
            R.append(arr[q+j+1])
        i = 0
        j = 0
        k = p

        while i<nL and j < nR:
            self.comparison_count += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < nL:
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j< nR:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, p, r):
        if p >= r:
            return

        q = (p+r)//2
        self.merge_sort(p,q)
        self.merge_sort(q+1,r)
        self.merge(p,q,r)

    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def max_heapify(self, heap_size,i):
            l = self.left(i)
            r = self.right(i)
            largest = i
            if l < heap_size:
                self.comparison_count += 1
                if self.sorting_array[l] > self.sorting_array[i]:
                   largest = l
            # else:
                   

            if r < heap_size:
                self.comparison_count += 1
                if self.sorting_array[r] > self.sorting_array[largest]:
                    largest = r

            if largest != i:
                self.sorting_array[i], self.sorting_array[largest] = self.sorting_array[largest], self.sorting_array[i]
                self.max_heapify(heap_size,largest)

    def build_max_heap(self, n):
        pos = (n//2) - 1
        while pos >= 0:
            self.max_heapify(n, pos)
            pos -= 1
    
    def heap_sort(self):
        n = len(self.sorting_array)
        self.build_max_heap(n)
        for i in range(n-1,0,-1):
            self.sorting_array[0], self.sorting_array[i] = self.sorting_array[i], self.sorting_array[0]
            # n -= 1
            self.max_heapify(i, 0)

    def insertion_sort(self):
        arr = self.sorting_array
        count = self.comparison_count
        n = len(arr)
        for i in range(1,n):
            x = arr[i]
            j = i-1
            while j >= 0 and arr[j]>x:
                count += 1
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = x
            if j >= 0:
                count += 1
        self.comparison_count = count



        
