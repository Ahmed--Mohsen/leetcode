class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		if numRows <= 0:
			return []
			
		triangle = []
		for	row in range(0, numRows): 
			triangle_row = [1]*(row + 1)
			for i in range(1, len(triangle_row) - 1):
				prev_row = triangle[row - 1]
				triangle_row[i] = prev_row[i - 1] + prev_row[i]
			triangle.append(triangle_row)
		return triangle


s = Solution()
print s.generate(5)