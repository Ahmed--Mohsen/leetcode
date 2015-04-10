class MinStack:
	
	def __init__(self):
		self.stack = []
		self.min_val = float("inf")
		
	# @param x, an integer
	# @return an integer
	def push(self, x):
		if len(self.stack) == 0:
			self.stack.append(0)
			self.min_val = x
		else:
			self.stack.append(x - self.min_val) #store the gap between x and min
			self.min_val = min(self.min_val, x)
		
	# @return nothing
	def pop(self):
		if len(self.stack) == 0:
			return
		poped = self.stack.pop(-1)
		if poped < 0: #this value was the min
			self.min_val = self.min_val - poped
				
		
	# @return an integer
	def top(self):
		top = self.stack[-1]
		if top > 0:
			return top + self.min_val #add the gap
		else: #top is the minimum
			return self.min_val
		
	# @return an integer
	def getMin(self):
		return self.min_val

s = MinStack()
s.push(-2)
s.push(0)
s.push(-1)

print s.top()
s.pop()
s.push(-5)
print s.getMin()
print s.getMin()
print s.stack