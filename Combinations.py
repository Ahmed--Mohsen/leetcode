"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

class Solution:
	
	# @return a list of lists of integers
	def combine(self, n, k):
		if n <= 0:
			return []
		result = []
		self.combine_helper(n, k, 1, [], result)
		return result
	
	
	def combine_helper(self, n, k, start, combination, result):
		
		# base case
		if k == 0:
			result.append(list(combination))
			return
			
		for i in range(start, n+1):
			combination.append(i)
			self.combine_helper(n, k - 1, i + 1, combination, result)
			combination.pop()


s = Solution()
print s.combine(4,2)