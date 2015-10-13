class Solution(object):
	
	"""
	:type num: int
	:rtype: bool
	"""
	def isUgly(self, num):
		for factor in (2, 3, 5):
			while num % factor == 0 and num > 0:
				num /= factor
		return num == 1
		