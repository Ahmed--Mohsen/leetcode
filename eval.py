class Solution:
	# @param tokens, a list of string
	# @return an integer
	def evalRPN(self, tokens):
		stack = []
		for token in tokens:
			if self.isOperator(token):
				b = stack.pop()
				a = stack.pop()
				c = self.calc(a, b, token)
				stack.append(c)
			else:
				stack.append(int(token))
		return stack.pop()
			
	def isOperator(self, op):
		if op == "+" or op == "-" or op == "*" or op == "/":
			return True
		return False
		
	def calc(self, a, b, op):
		if op == "+":
			return a+b
		if op == "-":
			return a-b	
		if op == "*":
			return a*b
		if op == "/": #python weired division
			da = -1 * a if a < 0 else a
			db = -1 * b if b < 0 else b
			r = da/db
			if (a < 0 and b > 0) or (a > 0 and b < 0):
				r = -1 * r
			return r
			
s = Solution()
l = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print s.evalRPN(l)