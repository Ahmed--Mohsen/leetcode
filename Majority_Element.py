# -*- coding: utf-8 -*-
"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""

from collections import defaultdict

class Solution:
	
	# @param num, a list of integers
	# @return an integer
	def majorityElement(self, nums): # using moore voting alg.
		major = nums[0]
		vote = 1
		
		for i in range(1, len(nums)):
			# no major so nums[i] become a major
			if vote == 0:
				major = nums[i]
				vote += 1
				
			# nums[i] is still a major, inc. its vote
			elif major == nums[i]:
				vote += 1
			
			# nums[i] is new candidate but with less vote
			# than major, dec. major vote
			else:
				vote -= 1
				
		return major
			
	
	# @param num, a list of integers
	# @return an integer
	def majorityElementBit(self, nums): # using bit manipulation
		int_size = 32
		majority_element = 0
		
		# loop over each bit
		for i in range(int_size): 
			zero_count = 0
			one_count = 0

			# check i(th) bit for all
			for num in nums: 
				if abs(num) & (1 << i) != 0: # i(th) bit is one
					one_count += 1
				else:
					zero_count += 1
					
			# majority element i(th) bit is the bit with the larger count
			if one_count > zero_count:
				majority_element = majority_element | (1 << i)
			else:
				majority_element = majority_element & ~(1 << i)
		
		# check if majority element is negative or positive
		# this is not needed in java 
		negative_count = 0
		for num in nums:
			if num < 0:
				negative_count += 1
		
		# major element is negative number
		if negative_count > len(nums) / 2:
			majority_element = -1 * majority_element
			
		return majority_element
	
	
	
	# @param num, a list of integers
	# @return an integer
	def majorityElementHash(self, nums): # use hash
		n = len(nums)
		if n == 1: # base case
			return nums[0]
			
		target = int(len(nums)/2.0)
		count = defaultdict(int) # key = number, value = number of appearance
		
		for num in nums:
			count[num] += 1
			if count[num] > target:
				return num


s = Solution()
print s.majorityElement([6,5,5])
			