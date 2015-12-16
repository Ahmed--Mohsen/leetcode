"""

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""

class Solution:
	
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		n = len(triangle)
		
		# start with the minimum path at the bottom layer
		minPath = list(triangle[-1]) 
		
		# loop on layers
		for layer in range(n-2, -1, -1): 
			
			# loop on children
			for i in range(0, layer+1): 
				minPath[i] = min( minPath[i], minPath[i+1] ) + triangle[layer][i]
		
		return minPath[0]