"""

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""

from collections import defaultdict

class Solution:
	
	# @return a string
	def minWindow(self, S, T):
		s_len = len(S)
		t_len = len(T)
				
		# store count per char in t
		needed = defaultdict(int)
		for i in range(t_len):
			needed[T[i]] += 1
		
		# total count of chars in S that are already in T
		count = 0 
		
		# keep track of min windows so far
		min_len = float("inf")
		min_index = 0
		
		# left boundries for window
		start = 0
		
		# advance end pointer for 0 to lenght of S
		# each char will be visited at most twice once
		# by start and another by end => O(2n) = O(n)
		for end in range(s_len):
			needed[S[end]] -= 1
			
			# check if S[end] is actually needed to match T
			if needed[S[end]] >= 0:
				count += 1
				
			# while the window contains all chars in T
			while count == t_len:
				
				# update min window
				if end - start + 1 < min_len:
					min_len = end - start + 1
					min_index = start
				
				# move start pointer one step
				needed[S[start]] += 1
				if needed[S[start]] > 0: # S[start] was needed
					count -= 1
				start += 1
		
		if min_len == float("inf"): # not found
			return ""
		return S[min_index: min_index + min_len]
		
			

s = Solution()		
print s.minWindow("ADOBECODEBANC", "ABC")
#print s.minWindow("acbbaca", "aba")
			
			
			
			