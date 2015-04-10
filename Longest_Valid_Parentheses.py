class Solution:
	# @param s, a string
	# @return an integer
	def longestValidParentheses(self, s):
		if s == None or len(s) == 0:
			return 0
		
		last = -1
		stack = []
		max_len = 0
		for i in range(len(s)):
			if s[i] == "(":
				stack.append(i)
			else: #s[i] == ")"
				if len(stack) == 0: #new start
					last = i
				else:
					stack.pop()
					
					#if stack is empty mean the positon before the valid left parenthesis is "last"
					if len(stack) == 0:
						max_len = max(max_len, i - last )
					else:
						#stack is not empty
						max_len = max(max_len, i - stack[-1])
		return max_len
				

s = Solution()
print s.longestValidParentheses("()")