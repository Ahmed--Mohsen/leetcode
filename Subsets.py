class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, S):
		if S == None: #base case
			return S
		
		S.sort()
		n = len(S)
		result = []
		total = (1 << n)
		for i in range(total):
			#create a subset based on binary representation
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