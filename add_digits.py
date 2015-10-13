class Solution(object):
	
	"""
	:type num: int
	:rtype: int
	"""
	def addDigits(self, num):
		# base case
		if num == 0:
			return 0
		
		return num - (9 * ( (num - 1) / 9 ))
	
	
	"""
	:type num: int
	:rtype: int
	"""
	def addDigitsIterative(self, num):
		
		while num > 9:
			total = 0
			
			# sum the digits
			while num:
				total += (num % 10)
				num /= 10
			
			num = total
		
		return num


s = Solution()
print s.addDigits(2)

#for i in range(10,200):
	#print i, s.addDigits(i)
		
		
			
			
			
