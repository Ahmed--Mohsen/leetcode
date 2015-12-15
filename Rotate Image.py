"""

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

brute force: 	new_matrix[j][height - 1 - i] = matrix[i][j]
"""

class Solution:
	
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	def rotate(self, matrix):
		
		# base case
		if matrix == None: return None
		
	  # clockwise rotate
	  # first reverse up to down, then swap the symmetry 
	  # 1 2 3     7 8 9     7 4 1
	  # 4 5 6  => 4 5 6  => 8 5 2
	  # 7 8 9     1 2 3     9 6 3
		
		# up to down reverse
		matrix.reverse()

		# move on the diagonal and swap elements 
		for i in range(len(matrix)):
			for j in range(i):
				matrix[i][j], matrix[j][i] = matrix[j][i] ,matrix[i][j]
