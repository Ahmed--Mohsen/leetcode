"""

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution:
	
	# @return an integer
	def romanToInt(self, s):
		map = {
			'I' : 1,
			'V' : 5,
			'X' : 10,
			'L' : 50,
			'C' : 100,
			'D' : 500,
			'M' : 1000
		}
		result = 0
		prev_int = 0
		
		for i in range(len(s) -1 , -1, -1):
			c = s[i]
			current_int = map[c]
			if current_int >= prev_int:
				result += current_int
			else:
				result -= current_int
			prev_int = current_int

		return result


s = Solution()
print s.romanToInt("MMMDLXXXVI")