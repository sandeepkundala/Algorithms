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
	def heapify(A, n, i): 
	    largest = i 
    	    left = 2 * i + 1 
    	    right = 2 * i + 2  
    	    
	    self.comparison_count+=1 
    	    if left < n and A[largest] < A[left]: 
                largest = left
	    if left >= n:
                self.comparison_count-=1
 
  	    self.comparison_count+=1
    	    if right < n and A[largest] < A[right]: 
                largest = right
	    if right >= n:
                self.comparison_count-=1
    	    if largest != i: 
                A[i], A[largest] = A[largest], A[i]
                heapify(A, n, largest)	
               
	n = len(self.sorting_array)  
    	for i in range(n, -1, -1): 
            heapify(self.sorting_array,n, i) 

    	for i in range(n-1, 0, -1): 
            self.sorting_array[i], self.sorting_array[0] = self.sorting_array[0], self.sorting_array[i] 
            heapify(self.sorting_array,i, 0) 

    
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
