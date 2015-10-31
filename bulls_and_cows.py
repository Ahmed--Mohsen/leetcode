class Solution(object):
	
	"""
	:type secret: str
	:type guess: str
	:rtype: str
	"""
	def getHint(self, secret, guess):
		
		# base case
		if len(secret) == 0:
			return "0A0B"
			
		bull = 0
		cows = 0
		
		memo = [0] * 10
		
		for i in range(len(secret)):
			s = ord(secret[i]) - ord('0')
			g = ord(guess[i]) - ord('0')
			if s == g:
				bull += 1
			else:
				# if g has not been covered before by s
				if memo[s] < 0: cows += 1
				if memo[g] > 0: cows += 1
				
				memo[s] += 1
				memo[g] -= 1 
		
		return "%dA%dB"%(bull, cows)


s = Solution()
print s.getHint("1807" ,"7810")