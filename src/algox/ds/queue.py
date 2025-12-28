class Queue:
	def __init__(self, arr=None):
		self._queue = []
		self.len = 0
		
		if arr:
			self._build(arr)
	
	def _build(self, arr):
		if self.is_empty():
			for element in arr:
				self._queue.append(element)
				self.len += 1

	def is_empty(self):
		return self.len == 0

	def enqueue(self, data):
		self._queue = [data] + self._queue
		self.len += 1
	
	def dequeue(self):
		if self.is_empty(): return None
		item = self._queue[-1]
		del self._queue[-1]
		self.len += 1
		return item
		
	def __repr__(self):
		if self.is_empty():
			return "Queue()"
		return f"Queue(| {' | '.join(map(str, self._queue))} |)"
	
	def __len__(self):
		return self.len
	
	def __iter__(self):
		if self.is_empty(): return
		for item in self._queue:
			yield item

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# Queue (FIFO)
class LinkedQueue:
	def __init__(self, arr):
		self.head = None
		self.tail = None
		self.len = 0 
		
		if arr:
			self.build(arr)
	
	def build(self, arr):
		if not arr: return None
		self.head = self.tail = Node(arr[0])
		self.len = 1
		
		for element in arr[1:]:
			new_node = Node(element)
			self.tail.next = new_node
			self.tail = new_node
			self.len += 1
			
	# add an item to the back of the queue.
	def enqueue(self, data):
		if not self.head: return 
		
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node
		self.len += 1
	
	# remove and return the item from the front of the queue.
	def dequeue(self):
		if not self.head: return
		
		item = self.head.data
		self.head = self.head.next
		self.len -= 1
		return item
		
	# see the item at the front without removing it
	def peek(self):
		return self.head.data
	
	# get the number of items in the queue
	def size(self):
		return self.len
		
	# check if the queue is empty
	def is_empty(self):
		return self.len == 0
		
	def __len__(self):
		return self.len
	
	def __iter__(self):
		if not self.head: return 
		current = self.head
		
		while current:
			yield current.data
			current = current.next
		
	def __repr__(self):
		if not self.head: return "LinkedQueue()"
		str = ""
		current = self.head
		
		while current:
			str += f"| {current.data} "
			current = current.next
			
		return f"LinkedQueue({str}|)"