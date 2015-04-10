class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate_old(self, matrix):
		if matrix == None:
			return None
		height = len(matrix)
		width = len(matrix[0])
		new_matrix = [[0]*height for i in range(width)]		
		for i in range(height):
			for j in range(width):
				new_matrix[j][height - 1 - i] = matrix[i][j]
		return new_matrix
		

	def print_image(self, matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				print matrix[i][j],"   ",
			print "\n"
	
	

s = Solution()
x = []
current = 1
for i in range(4):
	y = []
	for j in range(3):
		y.append(current)
		current += 1
	x.append(y)
s.print_image(x)
ans = s.rotate(x)
s.print_image(ans)