class Solution:
	# @return a boolean
	def isMatch(self, str, pattern):
		s = 0; p = 0
		match_index = 0; star_index = -1
		
		while s < len(str):
			#advancing both pointers
			if p < len(pattern) and (pattern[p] == "?" or pattern[p] == str[s]):
				s += 1
				p += 1
				
			#* found, only advancing pattern pointer
			elif p < len(pattern) and pattern[p] == "*":
				star_index = p
				match_index = s
				p += 1
				
			#last pattern pointer was *, advancing string pointer
			elif star_index != -1:
				p = star_index + 1
				match_index += 1
				s = match_index
				
			#current pattern pointer is not star, last patter pointer was not *
			#chars don't match
			else:
				return False
				
		#check for remaining characters in pattern		
		while p < len(pattern) and pattern[p] == "*":
			p += 1
		
		return p == len(pattern)



############################## Another Solution ############################## 


class Solution:
	# @return a boolean
	def isMatchRecursive(self, s, p):
		#print s, " --- ", p
		if len(p) == 0:
			return len(s) == 0
		
		if len(p) > 1 and p[0] == "*" and len(s) == 0:
			return False
		
		if p[0] == "?" or s[0] == p[0]:
			return self.isMatch(s[1:], p[1:])
			
		if p[0] == "*":
			return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
			