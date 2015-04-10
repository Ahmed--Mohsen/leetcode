class Solution:
	# @return a list of lists of integers
	def combine(self, n, k):
		if n <= 0:
			return []
		self.result = []
		self.combine_helper(n, k, 1, [])
		return self.result
	
	
	def combine_helper(self, n, k, start, combination):
		#base case
		if k == 0:
			self.result.append(list(combination))
			return
			
		for i in range(start, n - (k-1) + 1):
			combination.append(i)
			self.combine_helper(n, k - 1, i + 1, combination)
			combination.remove(i)


s = Solution()
print s.combine(4,2)