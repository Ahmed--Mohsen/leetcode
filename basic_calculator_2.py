class Solution:
	# @param {string} s
	# @return {integer}
	def calculate(self, s):
		# empty case
		if len(s) == 0:
			return 0
			
		# do post fix transformation
		stack = []
		postfix = self.transform_postfix(s)
		
		for c in postfix:
			if str(c) in "+-/*": #operator
				b = stack.pop()
				a = stack.pop()
				if c == '+':
					result = a + b
				elif c == '-': 
					result = a - b
				elif c == '*':
					result = a * b
				else: # c == '/'
					result = a / b
				stack.append(result)
			else: # number
				stack.append(c)
				
		return stack.pop()
		
	def rank(self, operator):
		if operator == '*' or operator == '/':
			return 2
		elif operator == '+' or operator == '-':
			return 1
		else: # '('
			return 0
	
	def transform_postfix(self, s):
		# will hold the transformation
		postfix = []
		
		# will hold +, -, (
		operators = []
		
		# for buffering numbers
		num = 0
		prev_was_number = False
		
		for c in s:
			# escape empty chars
			if c == ' ':
				continue	
				
			# number or part of it
			if c >= '0' and c <= '9':
				num = num * 10 + int(c)
				prev_was_number = True
			else: # check if there was number buffering
				if prev_was_number:
					postfix.append(num)
					num = 0
					prev_was_number = False
				
			# nothing to be done here
			if c == '(':
				operators.append(c)
			
			# pop till matching '('
			elif c == ')':
				while operators[-1] != '(':
					postfix.append(operators.pop())
				operators.pop() # popping '('
			
			# operator pop till '('
			elif c in "+-/*":
				while operators and self.rank(operators[-1]) >= self.rank(c):
					postfix.append(operators.pop())
				operators.append(c)
		
		# check if the last operand was number
		if prev_was_number:
			postfix.append(num)
			
		# pop remaning operators
		while operators:
			postfix.append(operators.pop())
		
		return postfix
		

s = Solution()
print s.calculate("3+5 / 2 ")