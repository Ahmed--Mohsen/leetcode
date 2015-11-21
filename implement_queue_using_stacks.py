"""

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""

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