"""

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

"""


below_20 = ["", "One", "Two", "Three", "Four","Five","Six","Seven","Eight","Nine","Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
below_100 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

class Solution(object):

	"""
	:type num: int
	:rtype: str
	"""
	def numberToWords(self, num):
		# base case
		if num == 0:
			return "Zero"
		
		result = self.num_to_word(num)
		return result[1:]
		
	def num_to_word(self, num):
		if num >= 1000000000:
			return self.num_to_word(num / 1000000000) + " Billion" + self.num_to_word(num % 1000000000)
		elif num >= 1000000:
			return self.num_to_word(num / 1000000) + " Million" + self.num_to_word(num % 1000000)
		elif num >= 1000:
			return self.num_to_word(num / 1000) + " Thousand" + self.num_to_word(num % 1000)
		elif num >= 100:
			return self.num_to_word(num / 100) + " Hundred" + self.num_to_word(num % 100)
		elif num >= 20:
			return " " + below_100[num / 10] + self.num_to_word(num % 10)
		elif num >= 1:
			return " " + below_20[num]
		else:
			return ""


s = Solution()
print s.numberToWords(1234567891)
	