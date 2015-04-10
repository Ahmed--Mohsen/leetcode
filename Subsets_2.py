class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsetsWithDup(self, S):
		if S == None: #base case
			return S
		
		S.sort()
		n = len(S)
		result = [[]]
		i = 0
		
		while i < n:
			#count number of dupliactions
			duplicates = 0
			while i + duplicates < n and S[i+duplicates] == S[i]:
				duplicates += 1

			#get previous subsets created so far
		 	prev_subsets = len(result)
			for k in range(prev_subsets):
				subset = result[k]
				
				#and append i to it .. 0, 1, ..., duplicates
				for j in range(duplicates):
					subset = list(subset)
					subset.append(S[i])
					result.append(subset)
			
			i += duplicates #move to next uniqe number

		return result
			
s = Solution()
print s.subsetsWithDup([1,2,2])