class Solution:
	# @param s, a string
	# @return an integer
	def numDecodings(self, s):
		n = len(s)
		
		#base cases
		if n == 0:
			return 0
		if s[0] == "0":
			    return 0
	
		ways = [0] * (n+1) #ways[i] = num of ways to decode s[0:i]
		ways[0] = 1
		ways[1] = 1
		
		for i in range(2, n+1):
			num_1 = ord(s[i-1]) - ord("0")
			num_2 = int(s[i-2:i])
			ways[i] = ( ways[i-1] if num_1 > 0 else 0 ) + ( ways[i-2] if num_2 > 9 and num_2 <= 26 else 0)
			if ways[i] == 0:
				break
		return ways[n]