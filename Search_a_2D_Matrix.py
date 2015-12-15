"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

class Solution:
	
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		# base case
		if len(matrix) == 0: return False
		
		rows = len(matrix)
		colms = len(matrix[0])
		
		start = 0
		end = rows * colms - 1
		
		while start <= end:
			mid = (start + end) / 2
			
			# treating the matrix as a long 1D array (row major)
			mid_element = matrix[mid / colms][mid % colms]
			
			if mid_element == target:
				return True
			
			if mid_element > target:
				end = mid - 1
			else:
				start = mid + 1
				
		return False