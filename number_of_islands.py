class Solution:
	LAND = '1'
	
	# @param {character[][]} grid
	# @return {integer}
	def numIslands(self, grid):
		n = len(grid)
		if n == 0:
			return 0
		m = len(grid[0])

		# number of islands found
		islands_count = 1
		
		for i in range(n):
			for j in range(m):
				if grid[i][j] == self.LAND:
					islands_count += 1
					self.flood_fill(i, j, grid, str(islands_count))
		
		return islands_count - 1

	def flood_fill(self, i, j, grid, color):
		n = len(grid)
		m = len(grid[0])
		
		# mark this point as an island
		grid[i][j] = color
		
		# move up
		if i > 0 and grid[i-1][j] == self.LAND:
			self.flood_fill(i-1, j, grid, color)
		
		# move down
		if i < n - 1 and grid[i+1][j] == self.LAND:
			self.flood_fill(i+1, j, grid, color)
			
		# move left
		if j > 0 and grid[i][j-1] == self.LAND:
			self.flood_fill(i, j-1, grid, color)
						
		# move right
		if j < m - 1 and grid[i][j+1] == self.LAND:
			self.flood_fill(i, j+1, grid, color)
			
			
s = Solution()
inp = ["11000", "11000","00100","00011"]
inp = [[y for y in x] for x in inp]
print s.numIslands(inp)
