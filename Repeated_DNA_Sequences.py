from collections import defaultdict

class Solution:
	# @param s, a string
	# @return a list of strings
	def findRepeatedDnaSequences(self, s):
		n = len(s)
		memo = defaultdict(int)
		
		for i in range(n - 10 + 1): #get all substrings with len 10
			memo[s[i:i+10]] += 1

		return [key for key, value in memo.iteritems() if value > 1] #extract the keys with val > 1


s = Solution()
print s.findRepeatedDnaSequences("AAAAAAAAAAA")