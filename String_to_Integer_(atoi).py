class Solution:
	INT_MAX = 2147483647
	INT_MIN = -2147483648
	# @return an integer
	def atoi(self, str):		
		if str == None or len(str) == 0:
			return 0
		
		i = 0
		while i < len(str) and str[i] == ' ':
			i += 1
		str = str[i:]
	
		if len(str) == 0:
			return 0

		result = 0	
		sign = 1
		if str[0] == "-":
			str = str[1:]
			sign = -1
		elif str[0] == "+":
			str = str[1:]
		
		if len(str) > 0:
			if str[0] == "-" or str[0] == "+":
				return 0
				
		for i in range(0, len(str), 1):
			if self.valid_char(str[i]):
				num = ord(str[i]) - ord("0")
				result = (result * 10) + num
			else:
				break
		
		result = sign * result
		if result > self.INT_MAX:
			return self.INT_MAX
		elif result < self.INT_MIN:
			return self.INT_MIN
		return result
	
		
	def valid_char(self, char):
		if char == "-" or char == "+":
			return True
		return (ord(char) >= ord("0")) and (ord(char) <= ord("9"))
	

s = Solution()
print s.atoi("      asda-123")
			