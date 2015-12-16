"""

Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution:
	
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, S):
		n = len(S)
		
		# base case
		if not S: return S
		
		# first sort to ensure asc order
		S.sort()
		
		result = []
		
		# create a subset based on binary representation
		# from 0 till 2^n -1 ... 000 => 111 (n=3)
		total = (1 << n)
		
		for i in range(total):
			subset = []
			
			for j in range(n):
				if  ((i >> j) & 1) == 1:
					subset.append(S[j])
					
			result.append(subset)
			
		return result

s = Solution()
print s.subsets([1,2,2])

x = set()
x.add([1])