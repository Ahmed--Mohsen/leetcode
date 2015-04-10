class Solution:
	# @return an integer
	def numDistinct(self, S, T):
		m = len(S)
		n = len(T)
		
		memory = [0] * (n+1) # T in ""
		memory[-1] = 1 # "" in S
		
		for i in range(m-1, -1, -1):
			for j in range(n):
				if S[i] == T[j]:
					memory[j] += memory[j+1]
					
		return memory[0]