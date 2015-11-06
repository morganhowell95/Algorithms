class MinHeap:
	def __init__(self, arr=None):
		if not arr: self.heap = [0] 
		else: self.heap = [0] + arr
		self.size = 0
		self.buildHeap()

	def heapify(self, arr):
		#only need to heapify non leaves
		 i = len(arr)//2
		 self.heap = [0] + arr
		 self.size = len(arr)
		 while i > 0:
			 percDown(i)
			 i -= 1

	def percDown(self, i):
		while 2*i <= self.size:
			min_child = minChild(i)
			if self.heap[min_child] < self.heap[i]:
				temp = self.heap[min_child]
				self.heap[min_child] = self.heap[i]
				self.heap[i] = temp
			i = min_child

	def minChild(self, i):
		if (i*2)+1 > self.size:
			return i*2
		else:
			if self.heap[(i*2)+1]<self.heap[i*2]:
				return (i*2)+1
			else:
				return i*2

	def percUp(self, i):
		while i//2 > 0:
			if self.heap[i//2] > self.heap[i]:
				temp = self.heap[i//2]
				self.heap[i//2] = self.heap[i]
				self.heap[i] = temp
			i = i//2

	def insert(self, data):
		self.heap.append(data)
		self.size+=1
		self.percUp(self.size)

	def pop(self):
		el = self.heap[1]
		self.heap[1] = self.heap[self.size]
		self.heap.pop()
		self.size-=1
		percDown(1)
		return el
		

