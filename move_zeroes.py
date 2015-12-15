"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution(object):
	
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	def moveZeroes(self, nums):
		n = len(nums)
		
		# base case
		if n == 0: return

		# keep tracking of last filled position
		current = 0
		
		# loop till non empty is found and 
		# fill it in current position
		for i in range(n):
			if nums[i] != 0:
				nums[current] = nums[i]
				current += 1
		
		# set the remaning spaces with zeros
		while current < n:
			nums[current] = 0
			current += 1


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
