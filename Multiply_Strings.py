class Solution:
	# @param num1, a string
	# @param num2, a string
	# @return a string
	def multiply(self, num1, num2):
		l1 = len(num1)
		l2 = len(num2)
		s = [0] * (l1 + l2)
		
		for i in range(l1):
			carry = 0
			n1 = ord(num1[l1 - i - 1]) - ord('0')
			for j in range(l2):
				n2 = ord(num2[l2 - j - 1]) - ord('0')
				sum = n1*n2+s[i+j]+carry
				s[i+j] = sum%10
				carry = sum/10
			if carry > 0:
				s[i+l2] =+ carry
		
		
		start = l1+l2-1
		while(s[start] == 0 and start >= 0):
			start -= 1
		if start < 0:
			return "0"
		
		ans = ""
		for i in range(start, -1, -1):
			ans += str(s[i])
		return ans
				

s = Solution()
print s.multiply("0", "0")