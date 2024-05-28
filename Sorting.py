class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def bubble_sort(self):
        '''
        pushes the max element in each iteration of the outer loop by comparing the adjacent elements in inner loop
        TC : O(N^2) - worst, average
             O(N) - best
        '''
        n = len(self.sorting_array)
        for i in range(n-1,0,-1):
            isSwapped = 0
            for j in range(i):
                if self.sorting_array[j] > self.sorting_array[j+1]:
                    temp = self.sorting_array[j]
                    self.sorting_array[j+1] = self.sorting_array[j]
                    self.sorting_array[j] = temp
                    isSwapped = 1
            if isSwapped == 0:
                break
                


    def selection_sort(self):
        '''
        The array is divided into two parts: sorted half and unsorted half. In each iteration, the smallest element form the unsorted half is 
        selected and swapped with the firstvelement of the unsorted part of the array. In this way, the size of the sorted half increases and
        the arrays is sorted.
        TC: O(n^2) - Best, Worst, Average
        SC: O(1)
        '''
        n = len(self.sorting_array)
        for i in range(n-1):
            min_index = i
            for j in range(i, n):
                if self.sorting_array[j] < self.sorting_array[min_index]:
                    min_index = j
            self.sorting_array[i], self.sorting_array[min_index] = self.sorting_array[min_index], self.sorting_array[i]

    def insertion_sort(self):
        '''
        place the element in its correct position in the sorted left half in each iteration. Check the elements towards the left with the current
        element and swap until the current is placed in its correct postion.
        TC : O(N^2) - worst, average
             O(N) - best
        '''
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

    

arr = [1,]
sorting_algo = Sorting(arr)
sorting_algo.bubble_sort()
print(sorting_algo.sorting_array)


        
