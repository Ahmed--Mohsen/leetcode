class Solution:
	# @return a string
	def fractionToDecimal(self, n, d):
		#check zero numerator
		if n == 0:
			return "0"
		
		result = ""
		#check if result sign
		if bool(n < 0) != bool(d < 0):
			result += "-"
		
		n = abs(n)
		d = abs(d)
		
		#append integral part
		result +=  str(n/d)
		
		#check if fraction exist
		if n % d == 0:
			return result
		
		#start division
		result += "."
		seen = {}
		r = n % d #remainder
		
		while r > 0:
			#meet a known remainder
			if r in seen:
				pos = seen[r]
				result = result[:pos] + "(" + result[pos:] + ")"
				break
			
			#the remainder is first seen ... mark its position
			seen[r] = len(result)
			r *= 10
			result += str(r / d)
			r %= d
			
		return result
			
		
		
s = Solution()
print s.fractionToDecimal(2,3)