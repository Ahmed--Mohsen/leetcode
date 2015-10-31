ALPHAPET = 26

class Solution(object):
	
	"""
	:type s1: str
	:type s2: str
	:rtype: bool
	"""
	def isScramble(self, s1, s2):
		# base case ... no need to continue
		if len(s1) != len(s2):
			return False
			
		return self.isScrambleHelper(s1, s2, 0, 0, len(s1), {})

	def isScrambleHelper(self, s1, s2, i1, i2, len, cache):

		# check cache first 
		if (i1, i2, len) in cache:
			return cache[(i1, i2, len)]
		
		# base case
		if len == 0:
			cache[(i1, i2, len)] = True
			return True
		
		# s1 and s2 are single char strings
		if len == 1 and s1[i1] == s2[i2]:
			cache[(i1, i2, len)] = True
			return True
			
		# make sure both strings have the same chars (prunning)
		count = [0] * ALPHAPET
		
		for k in range(len):
			count[ord(s1[i1+k]) - ord('a')] += 1
			count[ord(s2[i2+k]) - ord('a')] -= 1
			
			
		# if any entry still has value so 2 strings differ
		for i in range(ALPHAPET):
			if count[i] != 0:
				cache[(i1, i2, len)] = False
				return False
		
		# try all breaking points and check is splitted
		# strings are scramble too
		result = False
		for k in range(1, len):
			
			if result:	break

			# normal matching
			result |= self.isScrambleHelper(s1, s2, i1, i2, k, cache) and self.isScrambleHelper(s1, s2, i1+k, i2+k, len-k, cache)
			
			# reverse matching
			if not result:
				result |= self.isScrambleHelper(s1, s2, i1, i2+k, len-k, cache) and self.isScrambleHelper(s1, s2, i1+len-k, i2, k, cache)
		
		# failure fallback
		cache[(i1, i2, len)] = result
		return result
		
		
s = Solution()
print s.isScramble("great", "rgtae")