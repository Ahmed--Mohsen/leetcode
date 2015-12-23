# -*- coding: utf-8 -*-
"""

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""

class NumArray(object):
	
	"""
	initialize your data structure here.
	:type nums: List[int]
	"""
	def __init__(self, nums):
		self.nums = nums
		
		# accumalate summing
		for i in range(1, len(nums)):
			self.nums[i] += self.nums[i - 1]

	"""
	sum of elements nums[i..j], inclusive.
	:type i: int
	:type j: int
	:rtype: int
	"""
	def sumRange(self, i, j):
		# base case
		if i == 0:
			return self.nums[j]
			
		return self.nums[j] - self.nums[i-1]


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 2)
print numArray.sumRange(0, 5)