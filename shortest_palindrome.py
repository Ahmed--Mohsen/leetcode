"""

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

"""

class Solution:
	# @param {string} s
	# @return {string}
	def shortestPalindrome(self, s):
		
		# s[::-1] is the reverse of s
		reverse_s = s[::-1]
		
		# make txt in this format to take advantage 
		# of KMP failure function (# is added for the 
		# case when s is plandirom iteself)
		txt = s + "#" + reverse_s
		
		# we want to find the largest suffix of the reversed string
		# that matches the prefix of the original string
		p = self.build_failure_table(txt)
		
		# p[-1] contains the start index of the largest suffix of reverse 
		# string that is similar to the prefix of the original
		# so this part [p[-1],size(reverse_s)] can be removed to 
		# get the minimal addition 
		minimal_add = reverse_s[ 0 : len(s) - p[-1] ]
		
		return minimal_add + s


	# build the failure function table of the KMP algorithm
	def build_failure_table(self, txt):
		
		n = len(txt)
		
		# init the table
		p = [0] * n
		
		for i in range(1, n):
			j = p[i-1]
			
			# search for best partial match
			while j > 0 and txt[i] != txt[j]:
				j = p[j-1]
			p[i] = j + (1 if txt[i] == txt[j] else 0)
			
		return p
				

s = Solution()
print s.shortestPalindrome("aacecaaa")