"""

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""

class Solution:
	
	# @param num, a list of integers
	# @return a string
	def largestNumber(self, num):
		str_num = map(str, num)
		str_num.sort(cmp=string_cmp)
		largest =  "".join(str_num)
		return largest if largest[0] != "0" else "0"
		
def string_cmp(s1, s2):
	s12 = s1 + s2
	s21 = s2 + s1
	return cmp(s21, s12)
	

s = Solution()
print s.largestNumber([2, 10])