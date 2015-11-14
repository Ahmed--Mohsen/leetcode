"""

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""

class Solution:
	
	# @param s, a string
	# @return an integer
	def numDecodings(self, s):
		n = len(s)
		
		#base cases
		if n == 0: return 0
		if s[0] == "0": return 0
	
		# ways[i] = num of ways to decode s[0:i]
		ways = [0] * (n+1) 
		ways[0] = 1
		ways[1] = 1
		
		for i in range(2, n+1):
			num_1 = int(s[i-1])
			num_2 = int(s[i-2:i])
			ways[i] = ( ways[i-1] if num_1 > 0 else 0 ) + ( ways[i-2] if num_2 > 9 and num_2 <= 26 else 0)
			if ways[i] == 0:
				break

		return ways[n]