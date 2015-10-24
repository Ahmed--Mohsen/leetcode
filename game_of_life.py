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