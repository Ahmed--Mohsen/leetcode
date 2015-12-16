"""

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""

class Solution:
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.
	def solve(self, board):
		row = len(board)
		if row == 0:
			return
		col = len(board[0])

		not_surround = [[False for j in xrange(0,col)] for i in xrange(0,row)]
		queue = []

		#move on the boundries
		for i in range(0, col): 
			
			# upper baoubdry
			if board[0][i] == 'O': 
				not_surround[0][i] = True
				queue.append((0, i))
			
			# lower baoubdry
			if board[row-1][i] == 'O': 
				not_surround[row-1][i] = True
				queue.append((row-1, i))
		
		
		for j in range(0, row): 
			
			# left baoubdry
			if board[j][0] == 'O': 
				not_surround[j][0] = True
				queue.append((j, 0))
			
			# right baoubdry
			if board[j][col-1] == 'O': 
				not_surround[j][col-1] = True
				queue.append((j, col-1))
		
		# start BFS
		while queue:
			start = queue.pop()
			i = start[0]
			j = start[1]
			
			# check up
			if i-1 > 0 and board[i-1][j] == 'O' and not_surround[i-1][j] == False: 
				not_surround[i-1][j] = True
				queue.append((i-1, j))
				
			# check down
			if i + 1 < row - 1 and board[i+1][j] == 'O' and not_surround[i+1][j] == False: 
				not_surround[i+1][j] = True
				queue.append((i+1, j))
				
			# check left
			if j - 1 >0 and board[i][j-1] == 'O' and not_surround[i][j-1] == False: 
				not_surround[i][j-1] = True
				queue.append((i, j-1))
			
			# check right
			if j + 1 < col - 1 and board[i][j+1] == 'O' and not_surround[i][j+1] == False: 
				not_surround[i][j+1] = True
				queue.append((i, j+1))
		
		# flip O to x if surrounded
		for	i in range(0, row):
			for j in range(0, col):
				if board[i][j] == 'O' and not_surround[i][j] == False:
					board[i][j] = 'X'
					
		return