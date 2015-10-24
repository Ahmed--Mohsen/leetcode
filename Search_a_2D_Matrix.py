class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		if len(matrix) == 0:
			return False
		
		rows = len(matrix)
		colms = len(matrix[0])
		
		start = 0
		end = rows * colms - 1
		
		while start <= end:
			mid = (start + end)/2
			# treating the matrix as a long 1D array (row major)
			mid_element = matrix[mid / colms][mid % colms]
			
			if mid_element == target:
				return True
			
			if mid_element > target:
				end = mid - 1
			else:
				start = mid + 1
				
		return False