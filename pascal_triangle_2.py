class Solution:
	# @return a list of lists of integers
	def getRow(self, rowIndex):
		if rowIndex < 0:
			return []
			
		for	row in range(0, rowIndex + 1): 
			triangle_row = [1]*(row + 1)
			for i in range(1, len(triangle_row) - 1):
				triangle_row[i] = prev_row[i - 1] + prev_row[i]
			prev_row = triangle_row
		return triangle_row


s = Solution()
print s.getRow(1)