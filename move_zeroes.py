class Solution(object):
	
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	def moveZeroes(self, nums):
		# base case
		if len(nums) == 0:
			return

		# keep tracking of last filled position
		current = 0
		
		# loop till non empty is found and 
		# fill it in current position
		for i in range(len(nums)):
			if nums[i] != 0:
				self.swap(nums, i, current)
				current += 1
	
	def swap(self, nums, i, j):
		temp = nums[i]
		nums[i] = nums[j]
		nums[j] = temp

s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
