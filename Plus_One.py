"""

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		# move backards
		for i in range(len(digits) - 1, -1, -1):
			
			# carry case
			if digits[i] == 9:
				digits[i] = 0
			
			# no need to continue after that will be added
			else:
				digits[i] += 1
				return digits 
				
		# if reached here there is a carry to be added
		# all digits are 9's
		digits[0] = 1
		digits.append(0)
			
		return digits

s = Solution()
print s.plusOne([9,9,9])