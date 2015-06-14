class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		n = len(nums)
		
		# base case (only one or less element)
		if n < 2:
			return False
		
		# save the first index occur for num
		memo = {}
		for i in range(n):
			# appeared before
			if nums[i] in memo:
				if i - memo[nums[i]] <= k: # at most k
					return True
					
			# save its index for latter comparison
			memo[nums[i]] = i
		
		# no solution found
		return False


s = Solution()
print s.containsNearbyDuplicate([1,2,3,4,1], 6)