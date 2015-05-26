class Solution:
	# @param {integer} s
	# @param {integer[]} nums
	# @return {integer}
	def minSubArrayLen(self, s, nums):
		# base case
		if s == 0 or len(nums) == 0:
			return 0
		
		# sliding window boundries
		left = 0; right = 0
		
		sum = 0; 
		min_len = float("inf")
		n = len(nums)
		
		while right < n:
			sum += nums[right]
			
			# check if left boundry needs to move too
			while sum >= s:
				min_len = min(min_len, right - left + 1)
				sum -= nums[left]
				left += 1
				
			# move the right boundry	
			right += 1
			
		return 0 if min_len == float("inf") else min_len


s = Solution()
print s.minSubArrayLen(7, [2,3,1,2,4,3])
			