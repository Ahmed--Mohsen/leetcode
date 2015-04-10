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
	if s12 > s21:
		return -1
	return 1
	

s = Solution()
print s.largestNumber([2, 10])