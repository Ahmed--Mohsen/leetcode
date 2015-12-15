"""

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

"""

############################## largest rectangle in histogram Solution ##############################
class Solution:

	# @param matrix, a list of lists of 1 length string
	# @return an integer
	def maximalRectangle(self, matrix):
		n = len(matrix)
	
		# base case
		if n == 0: return 0
	
		m = len(matrix[0])

		# keep track of the continous heights
		heights = [0] * m

		# the final result holder
		max_area = 0

		for i in range(n):
	
			# set the heights for each row (reset if got a zero)
			for j in range(m):
				heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
	
			# calc max area for histogram of rows [0, i]
			max_area = max(max_area, self.largestRectangleArea(heights))

		return max_area
		
	# @param height, a list of integer
	# @return an integer
	def largestRectangleArea(self, height):
		n = len(height)

		# base case
		if n == 0: return 0

		stack = []
		i = 0
		area = 0

		while i < n:
			# the peek of the stack is smaller than current hist[i]
			if len(stack) == 0 or height[stack[-1]] <= height[i]:
				stack.append(i)
				i += 1
			# height[i] is smaller than peek ... calc current area with peek as height
			else:
				tp = stack.pop(-1)
				width = i if len(stack) == 0 else i - stack[-1] - 1
				area = max(area, height[tp] * width)

		# remaining heights
		while stack:
			tp = stack.pop(-1)
			width = i if len(stack) == 0 else i - stack[-1] - 1
			area = max(area, height[tp] * width)
	
		return area
		


	##########################################################################################	
	"""
		Another way that uses the max sub array matrix algorithm
	"""
	
	#give TLE on the last test case although its o(n^3)
	def maximalRectangle_maxSubMatrixMethod(self, matrix):
		if len(matrix) == 0:
			return 0
		
		rows = len(matrix)
		colms = len(matrix[0])
		self.sum = self.calc_sum_matrix(matrix)
		
		#search for max area
		global_max = 0
		for r1 in range(rows):
			for r2 in range(r1, rows):
				local_max = 0
				for c in range(colms):
					if matrix[r1][c] == "0": #already failed
						continue 
					area = self.get_area(r1, c, r2, c)
					full_area = self.get_full_area(r1, c, r2, c)
					if area == full_area:
						local_max  += max(area, 0)
						global_max = max(global_max, local_max)
		
		return global_max					
		
	def calc_sum_matrix(self, matrix):
		rows = len(matrix)
		colms = len(matrix[0])
		
		#create dp sum matrix
		sum = [[0]* colms for i in range(rows)]
		
		#fill upper row and left colmn
		sum[0][0] = self.to_i(matrix[0][0])
		for j in range(1, colms):
			sum[0][j] = self.to_i(matrix[0][j]) + sum[0][j-1]
		for i in range(1, rows):
			sum[i][0] = self.to_i(matrix[i][0]) + sum[i-1][0]
		
		#fill the remaining sum matrix
		for i in range(1, rows):
			for j in range(1, colms):
				sum[i][j] = self.to_i(matrix[i][j]) + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]
				
		return sum
		
	
	def to_i(self, char):
		return ord(char) - ord("0")
		
	"""
		gets the area of the rectangle starting form (r1,c1) and
		ending at (r2, c2)
	"""
	def get_area(self, r1, c1, r2, c2):
		top_right_corner = self.sum[r1-1][c2] if r1 > 0 else 0
		bottom_left_corner = self.sum[r2][c1-1] if c1 > 0 else 0
		top_left_corner = self.sum[r1-1][c1-1] if (r1 > 0 and c1 > 0) else 0
		return self.sum[r2][c2] - top_right_corner - bottom_left_corner + top_left_corner
	
	"""
		gets the area if the rectangle contains all ones
	"""
	def get_full_area(self, r1, c1, r2, c2):
		height = r2 - r1 + 1
		width = c2 - c1 + 1
		return height * width
		
	
	def print_matrix(self, matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				print matrix[i][j],
			print "\n" 

		
		




s = Solution()
m = [[0,0,0,0],[0,1,1,0], [0,1,1,0], [0,0,0,0]]
print s.maximalRectangle(m)