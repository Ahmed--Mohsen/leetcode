from collections import deque

class Solution(object):
	
	"""
	:type nums: List[int]
	:type k: int
	:rtype: List[int]
	"""
	def maxSlidingWindow(self, nums, k):
		n = len(nums)
		
		# base case
		if k == 0 or n == 0:
			return []

		window = deque( nums[0 : k] )
		max_window = [max(window)]
		
		# moving the window till the end
		for i in range(k, n):

			# shift window
			window.popleft()
			window.append(nums[i])
			
			# compare with max so far window
			max_window.append(max(window))
		
		return max_window

s = Solution()
s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)