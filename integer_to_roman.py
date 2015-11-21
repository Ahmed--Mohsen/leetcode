"""

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution(object):
	
	"""
	:type num: int
	:rtype: str
	"""
	def intToRoman(self, num):
		
		# each symbol corresponds to its value
		values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
		
		# do the conversion
		roman = []
		for i in range(len(values)):
			if num >= values[i]:
				multiples = num / values[i]
				roman.append(symbols[i] * multiples)
				num =  num % values[i]
		
		# convert list to string
		return "".join(roman)


s = Solution()
print s.intToRoman(2)