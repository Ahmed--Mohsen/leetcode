"""

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""

class Solution:
	
	# @return a list of lists of integers
	def getRow(self, rowIndex):
		# base case
		if rowIndex < 0: return []
			
		for	row in range(0, rowIndex + 1): 
			triangle_row = [1] * (row + 1)
			
			for i in range(1, len(triangle_row) - 1):
				triangle_row[i] = prev_row[i - 1] + prev_row[i]
			prev_row = triangle_row
		return triangle_row


s = Solution()
print s.getRow(1)