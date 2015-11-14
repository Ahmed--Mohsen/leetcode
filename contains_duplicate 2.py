"""

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

"""
class Solution:
	
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		n = len(nums)
		
		# base case (only one or less element)
		if k <= 0:
			return False
		
		# save window of size k: nums[i - k] to nums[i - 1]
		memo = set()
		for i in range(n):
			
			# keep track of k sized window
			if i > k:
				memo.remove(nums[i - k - 1])
			 
			# appeared before
			if nums[i] in memo:
					return True
					
			# save its index for latter comparison
			memo.add(nums[i])
		
		# no solution found
		return False


s = Solution()
print s.containsNearbyDuplicate([1,2,3,4,1], 6)