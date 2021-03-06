# -*- coding: utf-8 -*-
"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""


class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		# use 2 pointers from left and right sides
		left = 0
		right = len(s) - 1
		
		while left < right:

			# skip any non alphanumeric char
			while left < right and not s[left].isalnum():
				left += 1
			while left < right and not s[right].isalnum():
				right -= 1
			
			# early stop
			if s[left].lower() != s[right].lower():
				return False
			
			# move forward
			left += 1
			right -= 1
		
		# all is well
		return True
		
		

s = Solution()
print s.isPalindrome("a.A")