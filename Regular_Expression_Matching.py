class Solution:
	
	# @return a boolean
	def isMatch(self, s, p):
		if len(s) == 0 and len(p) == 0:
			return True
		
		#dp[i][j] means s[0:i] and p[0:j] are matched or not
		dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
		
	
		#two empty strings
		dp[0][0] = True
	
		#when p is empty they will not match
		for i in range(1, len(s)+1):
			dp[i][0] = False
	
		#when s is empty they can only match if current char is *
		for j in range(1, len(p)+1):
			if p[j-1] == "*" and j > 1:
				dp[0][j] = dp[0][j-2] #depends on previous match
			else:
				dp[0][j] = False
	
		#general case s and p are full
		for i in range(1, len(s)+1):
			for j in range(1, len(p)+1):
				if p[j-1] == s[i-1] or p[j-1] == ".":
					dp[i][j] = dp[i-1][j-1]
				elif p[j-1] == "*" and j > 1:
					if p[j-2] == s[i-1] or p[j-2] == ".":
						dp[i][j] = dp[i-1][j] or dp[i][j-2] or dp[i][j-1]
						#dp[i][j-2]   means * repeated multiple times
						#dp[i][j-2]   means * repeated zero times
						#dp[i][j-1]   means * repeated one time
					else:
						dp[i][j] = dp[i][j-2]
				else:
					dp[i][j] = False
	
		return dp[len(s)][len(p)]
	
	
####################### recursive solution #######################
	
	# @return a boolean
	def isMatch_recurive(self, s, p):
		#print s, " --- ", p
		if len(p) == 0:
			return len(s) == 0
		
		if len(p) > 1 and p[1] == "*": #zero or more chars can match
			return self.isMatch(s, p[2:]) or (self.is_first_char_match(s, p) and self.isMatch(s[1:], p))
		else: #current chars must match
			return self.is_first_char_match(s, p) and self.isMatch(s[1:], p[1:])
			
	
	def is_first_char_match(self, s, p):
		return (len(p) != 0 and len(s) != 0) and (p[0] == s[0] or p[0] == "." )
		
s = Solution()
print s.isMatch("aab", "c*a*b")
#print s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")