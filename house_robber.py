class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def rob(self, nums):
		n = len(nums)
		
		# base cases
		if n == 0: return 0
		if n == 1: return nums[0]
		if n == 2: return max(nums[0], nums[1])
		
		# general case only need to keep track of 2 prev states
		# dp_0 ... dp[i-2]
		# dp_1 ... dp[i-1]
		# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
		#dp = [0] * n
		dp_0 = nums[0]
		dp_1 = max(nums[0], nums[1])
		dp_2 = 0
		for i in range(2, n):
			dp_2 = max(dp_1, dp_0 + nums[i])
			dp_0 = dp_1
			dp_1 = dp_2
		
		return dp_1


s = Solution()
print s.rob([1,16,5,20])
		
		