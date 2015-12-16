"""

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsetsWithDup(self, S):
		# base case
		if S == None: return S
		
		S.sort()
		n = len(S)
		result = [[]]
		i = 0
		
		while i < n:
			# count number of dupliactions
			duplicates = 0
			while i + duplicates < n and S[i+duplicates] == S[i]:
				duplicates += 1

			# get previous subsets created so far
		 	prev_subsets = len(result)
			for k in range(prev_subsets):
				subset = result[k]
				
				# append i to it .. 0, 1, ..., duplicates
				for j in range(duplicates):
					subset = list(subset)
					subset.append(S[i])
					result.append(subset)
			
			# move to next uniqe number
			i += duplicates 

		return result
			
s = Solution()
print s.subsetsWithDup([1,2,2])