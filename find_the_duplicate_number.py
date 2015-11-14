"""

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""

class Solution(object):
	
	############### O(n) Solution ###############
	"""
	:type nums: List[int]
	:rtype: int
	"""
	def findDuplicate(self, nums):

		# using the same idea for finding cycles
		# in linked list by treating the index as source
		# and its value as distination
		slow = nums[0]
		fast = nums[nums[0]]
		
		while slow != fast:
			slow = nums[slow]
			fast = nums[nums[fast]]
		
		# now find the actual duplicate (cycle starter)
		slow = 0
		while slow != fast:
			slow = nums[slow]
			fast = nums[fast]
		
		return slow
	
	
	
	############### O(nlogn) Solution ###############
	"""
	:type nums: List[int]
	:rtype: int
	"""
	def findDuplicate(self, nums):
		n = len(nums)
		low, high = 0, n-1
		
		# do a binary search and count all occurances
		# for the mid element
		while low < high:
			mid = low + ((high-low) >> 1)
			
			# counting
			count = sum(num <= mid for num in nums)
			
			# if count is more than mid (left half is too crowded)
			if count > mid:
				high = mid
			
			# right is too crowded
			else:
				low = mid + 1
		
		return low