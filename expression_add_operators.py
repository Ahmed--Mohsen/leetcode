class Solution(object):
	
	"""
	:type num: str
	:type target: int
	:rtype: List[str]
	"""
	def addOperators(self, num, target):
		# base case
		if len(num) == 0:
			return []
		
		result = []
		self.addOperatorsHelper(num, "", 0, target, 0, 0, result)
		return result
		
	"""
	:type num: str
	:type target: int
	:type expr: string current expression built so far
	:type start: int the place were to continue processing
	:type value: int current value produced by expr
	:type prev: int last number proccesed to be used in expr
	:type result: List[str] containing the final result
	:rtype: void
	"""
	def addOperatorsHelper(self, num, expr, start, target, value, prev, result):
		if start == len(num):
			if value == target:
				result.append(expr)
			return
		
		
		for i in range(start, len(num)):
			# skip num starting with 0 like 02
			if i!= start and num[start] == "0": 
				break
				
			current = int(num[start:i+1])
			
			# the starting of new expression
			if start == 0:
				self.addOperatorsHelper(num, str(current), i+1, target, current, current, result)
			
			# try +, -, * (special case for higher precedence)
			else:
				self.addOperatorsHelper(num, expr+"+"+str(current), i+1, target, value + current, current, result)
				self.addOperatorsHelper(num, expr+"-"+str(current), i+1, target, value - current, -current, result)
				self.addOperatorsHelper(num, expr+"*"+str(current), i+1, target, (value - prev) + (prev * current), prev * current, result)

s = Solution()
print s.addOperators("1023", 23)