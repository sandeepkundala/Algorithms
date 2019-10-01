class Solution:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge_sort(self, p, r):
        def merge(p, q, r):
            n1 = q-p+1
            n2 = r-q
            Left = []
            Right = []
            for i in range(1, n1+1):
                Left.append(self.sorting_array[p+i-1])
            for i in range(1, n2+1):
                Right.append(self.sorting_array[q+i])
            Left.append(float('inf'))
            Right.append(float('inf'))
            i = 0
            j = 0
            for k in range(p, r+1):
                self.comparison_count = self.comparison_count + 1
                if Left[i] <= Right[j]:
                    self.sorting_array[k] = Left[i]
                    i = i + 1
                else:
                    self.sorting_array[k] = Right[j]
                    j = j + 1

        if p < r:
            q = int((p+r)/2)
            self.merge_sort(p, q)
            self.merge_sort(q+1, r)
            merge(p, q, r)


    def heap_sort(self):
        def buildMaxHeap():
            for i in range(int(len(self.sorting_array)/2), -1, -1):
                heapify(i)
        def heapify(i):
	    largest = i
    	left = 2 * i + 1
    	right = 2 * i + 2
        n = len(self.sorting_array)
    	if left <  n:
            self.comparison_count+=1
            if self.sorting_array[left] > self.sorting_array[i]:
                largest = l
            if right < heap_size:
                self.comparison_count+=1
                if self.sorting_array[r] > self.sorting_array[largest]:
                    largest = right
            if largest != i:
                self.sorting_array[i],self.sorting_array[largest] = self.sorting_array[largest],self.sorting_array[i]
                heapify(largest)
        buildMaxHeap()
        n = len(self.sorting_array)
    	for i in range((len(self.sorting_array)-1), 0, -1):
            tem = self.sorting_array[0]
            self.sorting_array[0] = self.sorting_array[i]
            self.sorting_array[i] = tem
            heap_size = heap_size - 1
            heapify(0)


    def insertion_sort(self):
        for i in range(1, len(self.sorting_array)):
            x = self.sorting_array[i]
            j = i - 1
            while j >= 0:
		self.comparison_count+=1
		if x < self.sorting_array[j]:
                	self.sorting_array[j + 1] = self.sorting_array[j]
			j -= 1
		else:
			break
            self.sorting_array[j + 1] = x
