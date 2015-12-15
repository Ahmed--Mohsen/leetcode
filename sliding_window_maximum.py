# -*- coding: utf-8 -*-
"""

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

Hint:

How about using a data structure such as deque (double-ended queue)?
The queue size need not be the same as the window’s size.
Remove redundant elements and the queue should store only elements that need to be considered.

"""

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
		
		# monotonic queue idea
		window = deque( [] )
		max_window = []
		
		# moving the window till the end
		for i in range(n):
			
			# remove out of range number
			if window and window[0] == i-k:
				window.popleft()
				
			# keep only elements that are larger than num[i]
			while window and nums[window[-1]] < nums[i]:
				window.pop()
			
			# append current element index (sorted now)
			window.append(i)
			
			# check if window size reached k
			if i >= k-1:
				max_window.append(nums[window[0]])
			
		return max_window

s = Solution()
print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)