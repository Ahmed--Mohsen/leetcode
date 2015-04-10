class Solution:
	# @return a boolean
	def isValid(self, s):
		#base case
		if s == None or len(s) == 0:
			return True
		
		stack = []
		for char in s:
			if self.is_opening_parentheses(char):
				stack.append(char)
			elif self.is_closing_parentheses(char):
				if len(stack) == 0:
					return False
				open_char = stack.pop(-1)
				if not self.match(open_char, char):
					return False
			else: #invalid char
				return False
		return len(stack) == 0
	
	def is_opening_parentheses(self, char):
		return char == "(" or char == "{" or char == "["
		
	def is_closing_parentheses(self, char):
		return char == ")" or char == "}" or char == "]"
	
	def match(self, open_char, close_char):
		case1 = open_char == "(" and close_char == ")"
		case2 = open_char == "{" and close_char == "}"
		case3 = open_char == "[" and close_char == "]"
		return case1 or case2 or case3

s = Solution()
print s.isValid("[(){}]")