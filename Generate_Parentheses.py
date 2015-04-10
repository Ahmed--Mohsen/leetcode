class Solution:

  # @param an integer
  # @return a list of string
	def generateParenthesis(self, n):
		result = []
		if n == 0:
			return result
		self.generate("", 0, 0, n, result)
		return result
	
	def generate(self, str, left, right, n, result):
		if left > n: #base case
			return
			
		if left == n and right == n:
			result.append(str)
		else:
			self.generate(str+"(", left+1, right, n, result)
			if left > right:
				self.generate(str+")", left, right+1, n, result)
				
		

s = Solution()
print s.generateParenthesis(3)