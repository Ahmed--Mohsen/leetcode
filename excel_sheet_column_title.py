class Solution:
	# @return a string
	def convertToTitle(self, num):
		result = ""
		
		while num > 0:
			result = self.to_char((num - 1) % 26) + result
			num = (num - 1) / 26
			
		return result
		
	def to_char(self, num):
		return chr(num + ord('A'))


s = Solution()
print s.convertToTitle(27)
		