"""

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

"""

class Solution:
	
	# @return a string
	def fractionToDecimal(self, n, d):
		
		# check zero numerator
		if n == 0:
			return "0"
		

		# check if result sign (XOR)
		result = ""
		if bool(n < 0) != bool(d < 0):
			result += "-"
		
		n = abs(n)
		d = abs(d)
		
		# append integral part
		result +=  str(n/d)
		
		# check if fraction exist
		if n % d == 0:
			return result
		
		# start division
		result += "."
		seen = {}
		r = n % d #remainder
		
		while r > 0:
			# meet a known remainder
			if r in seen:
				pos = seen[r]
				result = result[:pos] + "(" + result[pos:] + ")"
				break
			
			# the remainder is first seen ... mark its position
			seen[r] = len(result)
			
			# calc quotient
			r *= 10
			result += str(r / d)
			r %= d
			
		return result
			
		
		
s = Solution()
print s.fractionToDecimal(2,3)