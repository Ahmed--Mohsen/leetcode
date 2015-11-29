# -*- coding: utf-8 -*-
"""

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
The algorithm should run in linear time and in O(1) space.

"""

class Solution:
	
	# @param num, a list of integers
	# @param k, integer set to 3 cause the problem is n/3
	# @return  a list of integers
	def majorityElement(self, nums, k=3): 
		# k is used for generic handling (moore voting)
		
		n = len(nums)
		
		# base case
		if n < 0: return []
		
		# c candidate each with counter[i]
		c = k - 1 
		candidates = [0] * c
		counters = [0] * c
		
		# find nums that can be candidates
		for num in nums:
			voted = False
			
			# search for a candidate with no votes
			# or a prev voted candidate for num
			for i in range(c):
				if counters[i] == 0 or candidates[i] == num:
					counters[i] += 1
					candidates[i] = num
					voted = True
					break
				
			# check if no votes been given
			if not voted:
				for i in range(c):
					counters[i] -= 1
		
		# reset majority counters
		for i in range(c):
			counters[i] = 0
			
		# calculate real frequencies
		for num in nums:
			for i in range(c):
				if candidates[i] == num:
					counters[i] += 1
					break

		# choose those candidates that actually satisify [n/k] condition			
		result = []
		for i in range(c):
			if counters[i] > n / k:
				result.append(candidates[i])
			
		return result

		

s = Solution()
print s.majorityElement([3,2,3])
			