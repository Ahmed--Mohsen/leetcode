from collections import deque

class Stack:
	# initialize your data structure here.
	def __init__(self):
		self.queue = deque([])

	# @param x, an integer
	# @return nothing
	def push(self, x):
		self.queue.append(x)
		
		# rotate queue n - 1 times
		n = len(self.queue)
		for i in range(n-1):
			self.queue.append(self.queue.popleft())

	# @return nothing
	def pop(self):
		self.queue.popleft()

	# @return an integer
	def top(self):
		return self.queue[0]

	# @return an boolean
	def empty(self):
		return len(self.queue) == 0

s = Stack()
s.push(1)
print s.top()