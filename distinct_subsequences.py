"""

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

"""

####################### Space = O(n^2) time =  O(n^2) #######################
class Solution:
	
	# @return an integer
	def numDistinct(self, S, T):
		m = len(T)
		n = len(S)
		
		# memo[i+1][j+1] means that S[0..j] contains T[0..i] how much
		memo = [[0] * (m + 1) for i in range(n+1)]
		
		# memo[0][j] = 1, T is empty
		# mem[i][0] = 0, S is empty
		for j in range(n+1):
			memo[0][j] = 1
		
		# either ignore S[j-1] or consoder it
		for i in range(1, m+1):
			for j in range(1, n+1):
				memo[i][j] = memo[i][j-1] + (memo[i-1][j-1] if S[j-1] == T[i-1] else 0)
					
		return memo[m][n]
		
		
####################### Space = O(n) time =  O(n^2) #######################
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