"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

"""

class Solution:

  # @param an integer
  # @return a list of string
	def generateParenthesis(self, n):
		
		# base case
		if n == 0:
			return []
		
		result = []
		self.generate("", 0, 0, n, result)
		return result
	
	def generate(self, str, left, right, n, result):
		
		# all parenthesises are consumed
		if left == n and right == n:
			result.append(str)
			return
		
		# add '('
		if left < n:
			self.generate(str+"(", left+1, right, n, result)
		
		# add ')'
		if left > right:
			self.generate(str+")", left, right+1, n, result)
				

s = Solution()
print s.generateParenthesis(3)