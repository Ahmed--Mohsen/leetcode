"""

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

"""

############################### BFS Solution ###############################
class Solution:
	
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):		
		# base case
		if len(digits) < 1: return []
		
		# button to chars mapping
		mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		
		# the bfs queue in the current level
		result = [""]
		
		for digit in digits:
			num = ord(digit) - ord('0')
			chars = mapping[num]
			
			# update the result passed on prev state (level)
			tmp = []
			for r in result:
				for c in chars:
					tmp.append(r+c)
			result = tmp
			
		return result
	

############################### DFS Solution ###############################
class Solution:
	
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):		
		mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		result = []
		
		# base case
		if len(digits) < 1: 
			return result
		
		self.letterCombinationsHelper(mapping, digits, 0, [], result)
		return result
	
	def letterCombinationsHelper(self, mapping, digits, index, current, result):
		# base cases
		if index >= len(digits): 
			result.append("".join(current))
			return
		
		digit_map = mapping[ord(digits[index]) - ord('0')]
		for i in range(len(digit_map)):
			current.append(digit_map[i]) # try this combination
			self.letterCombinationsHelper(mapping, digits, index + 1, current, result) # recurse
			current.pop() # backtrack


s = Solution()
print s.letterCombinations("234")