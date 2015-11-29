"""

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""

class Solution:
	
	# @param s, a string
	# @return an integer
	def longestValidParentheses(self, s):
		n = len(s)
		
		# base case
		if n == 0: return 0
		
		stack = []
		longest = 0
		for i in range(n):
			if s[i] == "(":
				stack.append(i)
				
			else: # s[i] == ")"
				
				# s[i] can be matched so lets push it
				if stack and s[stack[-1]] == '(':
					stack.pop()
				
				# cannot be matched
				else:
					stack.append(i)
					

		# stack now have all indices that cannot be matched
		# find the longest string in between 2 invalid indices
		if len(stack) == 0: # all string is valid
			longest = n
		else:
			start = 0; end = n
			while stack:
				start = stack.pop(-1)
				longest = max(longest, end - start - 1)
				end = start
				
			# check the substring from 0 till end
			longest = max(longest, end)
						
		return longest
				


s = Solution()
print s.longestValidParentheses("(()()")