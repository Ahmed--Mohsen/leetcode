"""

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"""

from collections import defaultdict

class Solution:
	# @param s, a string
	# @return a list of strings
	def findRepeatedDnaSequences(self, s):
		n = len(s)
		memo = defaultdict(int)
		
		# get all substrings with len 10
		for i in range(n - 10 + 1): 
			memo[s[i:i+10]] += 1
		
		# extract the keys with val > 1
		return [key for key, value in memo.iteritems() if value > 1] 


s = Solution()
print s.findRepeatedDnaSequences("AAAAAAAAAAA")