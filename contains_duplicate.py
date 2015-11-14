"""

Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

"""
class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def containsDuplicate(self, nums):
		
		# base case
		if len(nums) < 2:
			return False
			
		# hash sets to be filled with nums
		memo = set()
		
		for num in nums:
			if num in memo:
				return True
			memo.add(num)
		
		return False


s = Solution()
print s.containsDuplicate([1,2,3])