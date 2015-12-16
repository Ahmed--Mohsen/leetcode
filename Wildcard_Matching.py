"""

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

"""

class Solution:
	
	# @return a boolean
	def isMatch(self, str, pattern):
		s = 0; p = 0
		match_index = 0; star_index = -1
		
		while s < len(str):
			
			# advancing both pointers
			if p < len(pattern) and (pattern[p] == "?" or pattern[p] == str[s]):
				s += 1
				p += 1
				
			# * found, only advancing pattern pointer
			elif p < len(pattern) and pattern[p] == "*":
				star_index = p
				match_index = s
				p += 1
				
			# last pattern pointer was *, advancing string pointer
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
		# base case
		if len(p) == 0:
			return len(s) == 0
		
		if len(p) > 1 and p[0] == "*" and len(s) == 0:
			return False
		
		if p[0] == "?" or s[0] == p[0]:
			return self.isMatch(s[1:], p[1:])
			
		if p[0] == "*":
			return self.isMatchRecursive(s, p[1:]) or self.isMatchRecursive(s[1:], p)
			