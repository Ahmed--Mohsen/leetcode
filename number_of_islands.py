"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

"""

class Solution:
	WATER = '0'
	LAND = '1'
	
	# @param {character[][]} grid
	# @return {integer}
	def numIslands(self, grid):
		n = len(grid)
		if n == 0:
			return 0
		m = len(grid[0])

		# number of islands found start with one to 
		# prevent confussion with the fact that lands are 
		# set to 1 already
		islands_count = 0
		
		# loop over all possible points
		for i in range(n):
			for j in range(m):
				
				# unvisited land .. visit it and all its neighbors
				if grid[i][j] == self.LAND:
					islands_count += 1
					self.flood_fill(i, j, grid)
		
		return islands_count

	def flood_fill(self, i, j, grid):
		n = len(grid)
		m = len(grid[0])
		
		# mark this point as a visited island (reset it to water)
		grid[i][j] = self.WATER
		
		# move up
		if i > 0 and grid[i-1][j] == self.LAND:
			self.flood_fill(i-1, j, grid)
		
		# move down
		if i < n - 1 and grid[i+1][j] == self.LAND:
			self.flood_fill(i+1, j, grid)
			
		# move left
		if j > 0 and grid[i][j-1] == self.LAND:
			self.flood_fill(i, j-1, grid)
						
		# move right
		if j < m - 1 and grid[i][j+1] == self.LAND:
			self.flood_fill(i, j+1, grid)
			
			
s = Solution()
inp = ["11000", "11000","00100","00011"]
inp = [[y for y in x] for x in inp]
print s.numIslands(inp)
