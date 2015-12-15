"""

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

class Solution:
	
	# @return a list of lists of integers
	def generate(self, numRows):
		# base case
		if numRows <= 0: return []
			
		triangle = []
		for	row in range(0, numRows):
			
			# init the row
			triangle_row = [1] * (row + 1)
			
			# calc the inner elements
			for i in range(1, len(triangle_row) - 1):
				prev_row = triangle[row - 1]
				triangle_row[i] = prev_row[i - 1] + prev_row[i]
			
			# done with this row
			triangle.append(triangle_row)
			
		return triangle


s = Solution()
print s.generate(5)