class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		carry = 1
		for i in range(len(digits) - 1, -1, -1):
			digit = digits[i]
			sum = (digits[i] + carry)
			digits[i] = sum%10
			carry = sum/10
			if carry == 0: #no need to continue
				break
		if carry > 0:
			digits = [carry] + digits
			
		return digits

s = Solution()
print s.plusOne([9,8,9])