class Queue(object):
	
	"""
	initialize your data structure here.
	"""
	def __init__(self):
		self.in_stack = []
		self.out_stack = []
	

	"""
	:type x: int
	:rtype: nothing
	"""
	def push(self, x):
		if x:
			self.in_stack.append(x)

	"""
	:rtype: nothing
	"""
	def pop(self):
		# check first if out stack cannot serve
		if not self.out_stack:
			self.reorder()
		
		# pop the element in place
		self.out_stack.pop()

	"""
	:rtype: int
	"""
	def peek(self):
		# for lazy insertion
		if not self.out_stack:
			self.reorder()
		
		return self.out_stack[-1]

	"""
	:rtype: bool
	"""
	def empty(self):
		return not (self.in_stack or self.out_stack)
	
	"""
	:rtype: nothing
	:doc: insert all elements in in_stack
				inside out_stack
	"""
	def reorder(self):
		# prepare all values in in_stack to be served
		while self.in_stack:
			self.out_stack.append(self.in_stack.pop())




q = Queue()
print q.empty()
q.push(1)
print q.empty()
q.push(2)
q.push(3)
print q.peek()
q.pop()
print q.peek()