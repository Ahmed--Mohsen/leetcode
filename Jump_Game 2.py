class Solution:
	# @param A, a list of integers
	# @return a boolean
	def jump(self, A):
		n = len(A)
		if n < 2:
			return 0
			
		level = 0
		i = 0
		current_max = 0
		next_max = 0

		while current_max - i + 1 > 0:  #num of nodes in current level > 0
			level += 1
			while i <= current_max:
				next_max = max(next_max, i + A[i])
				if next_max >= n - 1: #reached the end
					return level
				i += 1
			current_max = next_max
		return 0
			

s = Solution()
print s.jump([2,3,1,1,4])
		
		
		
				