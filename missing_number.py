"""

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""

class Solution(object):

	"""
	:type nums: List[int]
	:rtype: int
	"""
	def missingNumber(self, nums):
		n = len(nums)
		i = 0
		missing = 0
		
		# use the idea that xor remove duplicates
		for num in nums:
			missing ^= num
			missing ^= i # the missing number will fail to remove i
			i += 1
		
		# as the total elements are n+1 not only n
		missing ^= i
		
		return missing
		
		
			
	"""
	:type nums: List[int]
	:rtype: int
	"""
	def missingNumberFormula(self, nums):
		n = len(nums)
		
		# base case
		if n == 0:
			return 0
		
		# arethmetic series sum (n+1) elements
		# substitute in the general formula n(n-1)/2
		expected_sum = n * (n+1) / 2
		
		actual_sum = 0
		for num in nums:
			actual_sum += num
	
		return expected_sum - actual_sum