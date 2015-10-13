class Range(object):

	def __init__(self, start):
		super(Range, self).__init__()
		self.start = start
		self.end = start
	
	def can_merge(self, val):
		return val - self.end == 1
	
	def merge(self, val):
		self.end = val
	
	def __str__(self):
		# true range
		if self.start != self.end:
			return str(self.start) + "->" + str(self.end)
		else: # just single number
			return str(self.start)
		

class Solution:
	# @param {integer[]} nums
	# @return {string[]}
	def summaryRanges(self, nums):
		n = len(nums)
		
		# base case 
		if n == 0:
			return []
		
		# keep ranges in stack
		stack = [Range(nums[0])]
		for i in range(1, n):
			top = stack[-1]
			current = nums[i]
			
			# check if can be merged with latest range
			if top.can_merge(current):
				top.merge(current)
			
			# new range detected
			else:
				new_top = Range(current)
				stack.append(new_top)
		
		# return list of string representations for ranges
		return map(str, stack)

s = Solution()
print  s.summaryRanges([0,1,2,4,5,7])