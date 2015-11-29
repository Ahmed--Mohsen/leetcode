"""

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""

class Solution:
	
	# @param num, a list of integer
	# @return an integer
	def longestConsecutive(self, num):
		
		# base case
		if len(num) == 0:
			return 0
		
		# for O(1) element searching
		s = set(num)
		
		# means single element itself is a sequence
		max_count = 1
		
		# for each number move left and right to check
		# if there is a sequence
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