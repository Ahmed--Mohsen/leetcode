class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		if s in dict:
			return True
		
		can_break = [False]*(len(s) + 1) 
		can_break[0] = True
		
		for	i in range(len(s) + 1):
			
			if not can_break[i]:
				continue
				
			for string in dict:
				length = len(string)
				end = i + length
				if end > len(s): #can't break
					continue
					
				if can_break[end]: #calculated before
					continue
					
				if s[i:end] == string:
					can_break[end] = True
			
		return can_break[len(s)]
		
s = Solution()
ss = set()
ss.update(["leet", "code"]) 
print s.wordBreak("ss", ss)