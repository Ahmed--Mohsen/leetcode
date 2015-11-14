"""

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1- Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2- Any live cell with two or three live neighbors lives on to the next generation.
3- Any live cell with more than three live neighbors dies, as if by over-population..
4- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""

class Solution(object):
	
	"""
	:type board: List[List[int]]
	:rtype: void Do not return anything, modify board in-place instead.
	"""
	def gameOfLife(self, board):
		# base case
		if len(board) == 0:
			return
		
		m = len(board)
		n = len(board[0])
		
		# helper for returning number of live neighbors
		def get_neighbors(i, j):
			count = 0
			for r in range(max(i-1, 0), min(i+2, m)):
				for c in range(max(j-1, 0), min(j+2, n)):
					count += board[r][c] & 1
			return count
		
		# use the second rightmost bit to save the new state
		for i in range(m):
			for j in range(n):
				neighbors = get_neighbors(i,j)
				
				# (count == 3) is applying rule 2 (part1) & 4
				# (count - board[i][j] == 3) is applying rule 2 (part2) & 4
				if  neighbors == 3 or neighbors - board[i][j] == 3: 
					board[i][j] |= 2
			
		# shift the second bit to remove the old state 
		for i in range(m):
			for j in range(n): 
				board[i][j] >>= 1


s = Solution()
s.gameOfLife([[1,0,1], [0,1,0]])