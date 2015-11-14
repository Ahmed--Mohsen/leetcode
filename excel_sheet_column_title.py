"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

"""

class Solution:
	
	# @return a string
	def convertToTitle(self, num):
		result = ""
		
		while num > 0:
			num -= 1 # so 1 maps to A
			result = self.to_char(num  % 26) + result
			num /= 26
			
		return result
		
	def to_char(self, num):
		return chr(num + ord('A'))


s = Solution()
print s.convertToTitle(27)
		