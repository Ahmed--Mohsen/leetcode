"""

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""

class Solution:
	
	# @param {integer[]} nums
	# @return {integer}
	def rob(self, nums):
		n = len(nums)
		
		# base cases
		if n == 0: return 0
		if n == 1: return nums[0]
		
		# we have 2 options (1) rob house 0 (2) rob house n-1
		# (1) solve for interval [0, n-2] (leave house n-1)
		rob_first = self.rob_helper(nums, 0, n-2)
		
		# (2) solve for interval [1, n-1] (leave house 0)
		rob_last = self.rob_helper(nums, 1, n-1)
		
		# answer is the max of the 2 options
		return max(rob_first, rob_last)
	
	# @param {integer[]} nums
	# @param {integer} start
	# @param {integer} end
	# @return {integer}
	def rob_helper(self, nums, start, end):
		n = end - start + 1
		
		# base cases ... n < 2
		if n == 1: return nums[start]
		if n == 2: return max(nums[start], nums[start+1])
		
		# general case when n > 2
		# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
		#dp = [0] * n
		dp = [0] * n
		dp[0] = nums[start]
		dp[1] = max(nums[start], nums[start+1])
		for i in range(2, n):
			dp[i] = max(dp[i-1], dp[i-2] + nums[start+i])
		return dp[n-1]



s = Solution()
print s.rob([1,16,5,20])
		
		