"""

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

"""

import math

class Solution(object):

	###################### BFS Solution ######################
	"""
	:type n: int
	:rtype: int
	"""
	def numSquares(self, n):
		# base case
		if n <= 0:
			return 0
		
		# least squares hold the leasst numbers of 
		# perfect squares to make i
		least_squares = [float("inf")] * (n+1)
		least_squares[0] = 0
		
		# save all perfect squares less than n
		max_root = int(math.sqrt(n))
		perfect_squares = []
		for i in range(1, max_root + 1):
			perfect_squares.append(i * i)
			least_squares[i * i] = 1
		
		# already a perfect square
		if least_squares[n] == 1:
			return 1
		
		# Graph node 1...n
	  # Node j is connected to node i via an edge if  
	  # and only if either j = i + (a perfect square number) or 
	  # i = j + (a perfect square number).
		queue = []
		for sqrt in perfect_squares:
			queue.append(sqrt)
		
		# level by level BFS
		current_least = 1
		while queue:
			
			# mark as visited
			current_least += 1
			
			queue_len = len(queue)
			for i in range(queue_len):
				current = queue.pop(0)
				
				# try all possible perfect square
				for sqrt in perfect_squares:
					
					# reached distination
					if sqrt + current == n:
						return current_least
					
					# can be used and not visited before
					elif sqrt + current < n and least_squares[sqrt + current] == float("inf"):
						least_squares[sqrt + current] = current_least
						queue.append(sqrt+current)
					
					# limit exceeded
					elif sqrt + current > n:
						break
					
		return 0

	###################### DP Solution ######################
	"""
	:type n: int
	:rtype: int
	"""
	def numSquaresDP(self, n):
		# base case
		if n <= 0:
			return 0
		
		# least squares hold the leasst numbers of 
		# perfect squares to make i
		least_squares = [float("inf")] * (n+1)
		least_squares[0] = 0
		
		# loop over all number less than n
		for i in range(1, n+1):
			
			# loop over perfect squares less than i
			j = 1
			while j*j <= i:
				sqrt = j*j
				
				# is i already a perfect square or look for the least of using
				# sqrt in the summation
				least_squares[i] = min(least_squares[i], least_squares[i - sqrt] + 1)
				
				j += 1
		
		return least_squares[-1]
				

s = Solution()
print s.numSquares(12)
				
			
			
		
	