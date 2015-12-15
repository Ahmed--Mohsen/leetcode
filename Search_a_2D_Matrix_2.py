"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

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
		
		# out of range case
		if matrix[0][0] > target or target > matrix[rows-1][colms-1]:
			return False
		
		row = 0
		colm = colms - 1
		
		# step-wise linear search
		while row < rows and colm >= 0:
			# target found
			if target == matrix[row][colm]:
				return True
			
			# search for next move
			if matrix[row][colm] < target:
				row += 1
			else: # matrix[row][colm] > target
				colm -= 1
		
		return False
