"""

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

"""

class Solution:
	
	# @param num1, a string
	# @param num2, a string
	# @return a string
	def multiply(self, num1, num2):
		
		# parse strings
		num1 = [int(n) for n in num1]
		num2 = [int(n) for n in num2]
		
		l1 = len(num1)
		l2 = len(num2)
		s = [0] * (l1 + l2)

		# move in reverse order
		for i in range(l1-1, -1, -1):
			carry = 0

			for j in range(l2-1, -1, -1):		
				tmp = s[i+j+1] + (num1[i] * num2[j]) + carry
				s[i+j+1] = tmp % 10
				carry = tmp / 10

			s[i] =+ carry

		# get the first position the has zero
		start = 0
		while start < len(s) and s[start] == 0:
			start += 1
		
		# all zeros
		if start == len(s): 
			return "0"
		
		return "".join(str(n) for n in s[start:])
		

s = Solution()
print s.multiply("756", "0")