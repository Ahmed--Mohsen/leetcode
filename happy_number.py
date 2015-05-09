class Solution:
	# @param {integer} n
	# @return {boolean}
	def isHappy(self, n):
		# hold the numbers that have been calculated so far
		visited = set()
		
		while n != 1:
			# calc next happy iteration
			happy = 0
			while n > 0:
				diigit = n % 10
				happy += (diigit * diigit)
				n /= 10
			
			# check for cycles
			if happy in visited:
				return False
			
			# move to next iteration
			visited.add(happy)
			n = happy	
			
		return True
	
	

s = Solution()
print s.isHappy(19)