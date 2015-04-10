class Solution:
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):
		if len(digits) < 1:
			return [""]
		
		self.create_digit_mapping()
		self.digits = digits
		self.result = []
		self.letterCombinationsHelper(0, "")
		
		return self.result
	
	def letterCombinationsHelper(self, digit_index, current):
		if digit_index >= len(self.digits): #base cases
			self.result.append(current)
			return
		current_digit = self.digits[digit_index]
		current_digit_map = self.mapping[current_digit]
		for i in range(len(current_digit_map)):
			self.letterCombinationsHelper(digit_index + 1, current + current_digit_map[i])
		
		
	def create_digit_mapping(self):
		self.mapping = {}
		self.mapping["1"] = ""
		self.mapping["2"] = "abc"
		self.mapping["3"] = "def"
		self.mapping["4"] = "ghi"
		self.mapping["5"] = "jkl"
		self.mapping["6"] = "mno"
		self.mapping["7"] = "pqrs"
		self.mapping["8"] = "tuv"
		self.mapping["9"] = "wxyz"


s = Solution()
print s.letterCombinations("234")