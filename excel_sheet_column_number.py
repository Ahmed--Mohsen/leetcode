"""

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

"""

class Solution:
	
	# @return a string
	def titleToNumber(self, title):
		result = 0
		
		# same as number systems conversion
		for char in title:
			result = result * 26 + (ord(char) - ord('A') + 1)
		
		return result


s = Solution()
print s.titleToNumber("AB")
		