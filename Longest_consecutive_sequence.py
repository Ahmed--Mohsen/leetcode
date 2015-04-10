from sets import Set

class Solution:
	# @param num, a list of integer
	# @return an integer
	def longestConsecutive(self, num):
		s = set()
		
		if num == None or len(num) == 0:
			return 0
		
		for n in num:
			s.add(n)
		max_count = 1
		
		for n in num:
			left = n - 1
			right = n + 1
			count = 1
			
			while left in s:
				s.remove(left)
				left = left - 1
				count = count + 1
				
			while right in s:
				s.remove(right)
				right = right + 1
				count = count + 1
				
			max_count = max(max_count, count)
		return max_count
				
s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])