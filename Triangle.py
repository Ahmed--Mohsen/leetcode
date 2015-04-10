class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		n = len(triangle)
		
		#start with the minimum path at the bottom layer
		minPath = list(triangle[-1]) 
		
		for layer in range(n-2, -1, -1): #loop on layers
			for i in range(0, layer+1, 1): #loop on children
				minPath[i] = min( minPath[i], minPath[i+1] ) + triangle[layer][i]
		
		return minPath[0]