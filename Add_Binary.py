"""

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
class Solution:
	
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		
		# base cases
		if len(a) == 0 and len(b) == 0:
			return 0
		if len(a) == 0:
			return b
		if len(b) == 0:
			return a
			
		i = len(a)-1 ; j = len(b) - 1
		carry = 0
		sum = ""
		
		# loop as long as there is a remaining in the 2 num or a carry
		while i >= 0 or j >= 0 or carry != 0:
			x = int(a[i]) if i >= 0 else 0
			y = int(b[j]) if j >= 0 else 0

			sub_sum = x + y + carry
			sum = str(sub_sum % 2) + sum
			carry = sub_sum / 2
			
			i -= 1
			j -= 1

		return sum
			
s = Solution()
print s.addBinary("1010", "1011")